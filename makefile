# w64devkitで一発ビルドするための台本
build:
	cd C:/Users/Owner/Desktop/c_edu/c/python_renkei
	gcc -O2 -msse3 -I"C:/Users/Owner/AppData/Local/Programs/Python/Python313/include" main.c -L"C:/Users/Owner/AppData/Local/Programs/Python/Python313/libs" -lpython313 -o main.exe
	strip main.exe
