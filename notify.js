const { exec } = require('child_process');

/*
I know perfectly well that it could be better written. 

The use of shelljs would be much more advisable. 
More on this subject here: 

https://stackoverflow.com/questions/44647778/how-to-run-shell-script-file-using-nodejs

However, at the moment it has to stay that way. As a simple example, 
that you can call this notification script from the node application
to which you provide an argument, which is the message you want to send on telegram. 

*/

const myArgs = process.argv.slice(2);

let command;

if(myArgs.length > 0)
{
    let temp_message =  '"' + myArgs[0] + '"';
    command = "./notify.sh " + temp_message;
} else {
    command = './notify.sh';
}

var script = exec(command,
        (error, stdout, stderr) => {
            console.log(stdout);
            console.log(stderr);
            if (error !== null) {
                console.log(`exec error: ${error}`);
            }
        });
