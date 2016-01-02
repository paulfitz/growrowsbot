// Take a filename from argv,
// Take a sql command from stdin,
// Run sql command on file.

// Should move all this off file system if it grows up.

var fname = process.argv[2];
var fs = require('fs');
var msg = fs.readFileSync('/dev/stdin').toString();
msg = msg.replace('\n', ' ', msg);
msg = msg.replace('\r', ' ', msg);

var lockFile = require('lockfile')

lockFile.lock(fname + '.lock', {}, function (er) {
    var sql = require('sql.js');
    var output = "";
    var filebuffer = null;
    try {
        filebuffer = fs.readFileSync(fname);
    } catch(e) {
        // pass, will report error later
    }
    var db = new sql.Database(filebuffer);
    try {
        var results = db.exec(msg);
        if (results.length==1) {
            results = results[0];
        }
        if ('values' in results) {
            results = results['values'];
        }
        output = JSON.stringify(results);
    } catch (e) {
        output = e.toString();
    }
    var data = db.export();
    var buffer = new Buffer(data);
    var writeFileAtomic = require('write-file-atomic').sync;
    writeFileAtomic(fname, buffer, 'binary');
    console.log(output);

    lockFile.unlock(fname + '.lock', function (er) {
        // pass
    });
});
