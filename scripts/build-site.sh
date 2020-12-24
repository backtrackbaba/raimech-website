rm -rf ../build/**/**
echo "Cleared the old build files"
cd ../src
python app.py build
echo "Completed building the site"
