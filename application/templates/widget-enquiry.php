<?php
$to      = 'easetemplatesocial@gmail.com'; // Put in your email address here
$subject = "Enquiry Form - Sidebar Widget"; // The default subject. Will appear by default in all messages. Change this if you want.

// User info (DO NOT EDIT!)
$yourname     = stripslashes($_REQUEST['yourname']); // sender's name
$email    = stripslashes($_REQUEST['email']); // sender's email
$mobileno    = stripslashes($_REQUEST['mobileno']);
$selectvisa    = stripslashes($_REQUEST['selectvisa']);
$message = stripslashes($_REQUEST['message']);



// The message you will receive in your mailbox
// Each parts are commented to help you understand what it does exaclty.
// YOU DON'T NEED TO EDIT IT BELOW BUT IF YOU DO, DO IT WITH CAUTION!
$msg .= "Name: " . $yourname . "\r\n\n"; // add sender's name to the message
$msg .= "E-mail: " . $email . "\r\n\n"; // add sender's email to the message
$msg .= "Monile No: " . $mobileno . "\r\n\n"; // add sender's phone to the message
$msg .= "For Visa : " . $selectvisa . "\r\n\n"; // add sender's phone to the message
$msg .= "Messages: " . $message . "\r\n\n"; // add sender's checkboxes to the message
$msg .= "\r\n\n";

$mail = @mail($to, $subject, $msg, "From:" . $email); // This command sends the e-mail to the e-mail address contained in the $to variable

if ($mail) {
    header("Location:index.html");
} else {
    echo 'Message could not be sent!'; //This is the message that will be shown when an error occured: the message was not send
}

?>