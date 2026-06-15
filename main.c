#include <Python.h>
#include <stdio.h>

int main() { // C言語は int main() だ
    Py_Initialize();

    PyObject *name = PyUnicode_DecodeFSDefault("main");
    PyObject *module = PyImport_Import(name);
    
    // モジュールが読み込めたか確認（念のため）
    if (module == NULL) {
        PyErr_Print();
        return 1;
    }
    
    PyObject *func = PyObject_GetAttrString(module, "janken");

    int dasute;
    while (1) { // C言語は while(1) で無限ループだ
        printf("あなたの出す手は？(0:グー, 1:チョキ, 2:パー, -1で終了): ");
        if (scanf("%d", &dasute) != 1) break; // 入力失敗対策
        if (dasute == -1) break;

        PyObject *args = PyTuple_Pack(1, PyLong_FromLong(dasute));
        PyObject_CallObject(func, args);
        Py_DECREF(args);
    }

    Py_DECREF(func);
    Py_DECREF(module);
    Py_Finalize();
    return 0;
}