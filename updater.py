# wait one second to ensure main bb process has closed
#
# delete everything from install directory except the modules folder
#
# move the dist folder from the extracted update folder to the install folder
#
# run the installer with the appropriate args
#
# exit this process immediately in order to avoid a file lock when the installer - being
# aware that it was triggered as part of an update - runs cleanup to delete the downloaded
# zip, the extracted update, and the updater file along with any other leftover files from
# the update process