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

if [ $1 = deploy ]; then
    echo "Started deploy..."
    firebase deploy
fi

