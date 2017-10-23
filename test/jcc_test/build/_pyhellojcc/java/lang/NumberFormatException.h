#ifndef java_lang_NumberFormatException_H
#define java_lang_NumberFormatException_H

#include "java/lang/IllegalArgumentException.h"

namespace java {
  namespace lang {
    class String;
    class Class;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class NumberFormatException : public ::java::lang::IllegalArgumentException {
    public:
      enum {
        mid_init$_3b7a1d3d26162b85,
        mid_init$_38d57a80b9fe8948,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit NumberFormatException(jobject obj) : ::java::lang::IllegalArgumentException(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      NumberFormatException(const NumberFormatException& obj) : ::java::lang::IllegalArgumentException(obj) {}

      NumberFormatException();
      NumberFormatException(const ::java::lang::String &);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(NumberFormatException);

    class t_NumberFormatException {
    public:
      PyObject_HEAD
      NumberFormatException object;
      static PyObject *wrap_Object(const NumberFormatException&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
