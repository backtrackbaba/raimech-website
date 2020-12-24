rm -rf ../build/**/**
echo "Cleared the old build files"
python ../src/app.py build
echo "Completed building the site"
