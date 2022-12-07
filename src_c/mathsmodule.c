#define PY_SSIZE_T_CLEAN
#include <python3.10/Python.h>
#include <math.h>
typedef signed int int32_t;
typedef unsigned int uint32_t;
static const double one = 1.0, tiny = 1.0e-300;


static PyObject *
maths_sqrt(PyObject *self, PyObject *args)
{
    double num;

    if (!PyArg_ParseTuple(args, "d", &num))
    {
        return NULL;
    }

    int start = 0, end = num;
    int mid;
    double ans;
    while (start <= end) {
 
        mid = (start + end) / 2;
        if (mid * mid == num) {
            ans = mid;
            break;
        }
        if (mid * mid < num) {
            ans=start;
            start = mid + 1;
        }
 
        else {
            end = mid - 1;
        }
    }
 
    float increment = 0.1;
    for (int i = 0; i < 5; i++) {
        while (ans * ans <= num) {
            ans += increment;
        }
 
        ans = ans - increment;
        increment = increment / 10;
    }
    return PyFloat_FromDouble(ans);
}

static PyMethodDef MathsMethods[] = {
    {"sqrt", maths_sqrt, METH_VARARGS, "Python interface inline assmebly square root function"},
    {NULL, NULL, 0, NULL}};

static struct PyModuleDef maths_module = {
    PyModuleDef_HEAD_INIT,
    "maths",
    "Python interface inline assmebly square root function",
    -1,
    MathsMethods};

PyMODINIT_FUNC PyInit_maths(void)
{
    return PyModule_Create(&maths_module);
}
