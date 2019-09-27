python3 setup.py build_ext --inplace
pyinstaller --onefile "main.py"

echo ""
echo "Executable ./main will be generated to dist/"
echo ""

echo "Removing intermediate files..."

rm -fr build/ __pycache__/
find . -name "*.spec" -type f -delete
find . -name "*.so" -type f -delete
find . -name "*.c" -type f -delete

echo "Done."
