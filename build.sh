#!/bin/bash

# Build bookdown Script - By Adriano P. Almeida
# Last update: 21 September 2019

echo "Build started..."
echo "Open directory..."
cd docs
echo "done!"
echo  "Deleting old version.."
{
    rm -rf _book
    echo "done!"
} || {
    echo "There was an error deleting the folder!"
    exit 1
}

echo "Compiling bookdown..."
{
    Rscript -e "bookdown::render_book('index.Rmd', bookdown::gitbook(lib_dir = \
    'libs'))"
    echo "done!"
} || {
    echo "There was an error to build bookdown!"
    exit 1
}

{
    echo "open bookdown"
    google-chrome _book/index.html
} || {
    echo "There was an error to open bookdown!"
    exit 1
}

helpmenu() {
    echo "Usage: sh build.sh [OPTION]"
    echo "Script to compile and/or deploy bookdown "
    echo "\n"
    echo "Arguments."
    echo "   -h, --help \t\t flag to show help of script"
}

deployfirebase() {
    firebase deploy
    google-chrome https://cap-394.firebaseapp.com
}
while [ ! $# -eq 0 ]
do 
    case "$1" in 
        --help | -h)
            helpmenu
            exit
            ;;
        --deploy | -d)
            if [ ! -z $2 ]; then
                if [ $2 = firebase ]; then
                    echo "Deploy to firebase..."
                    deployfirebase      
                else
                    echo "Invalid option!"
                    echo "Pass one of the following arguments: \nfirebase"
                fi
            else
                echo "The deploy option is required!"
                echo "Pass one of the following arguments: \nfirebase"
            fi
			exit
			;;
    esac
    shift
done
