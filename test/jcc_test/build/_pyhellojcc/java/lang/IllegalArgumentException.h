#ifndef java_lang_IllegalArgumentException_H
#define java_lang_IllegalArgumentException_H

#include "java/lang/RuntimeException.h"

namespace java {
  namespace lang {
    class String;
    class Throwable;
    class Class;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class IllegalArgumentException : public ::java::lang::RuntimeException {
    public:
      enum {
        mid_init$_3b7a1d3d26162b85,
        mid_init$_359aa6a1d41f0219,
        mid_init$_38d57a80b9fe8948,
        mid_init$_5df017320dfbf543,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit IllegalArgumentException(jobject obj) : ::java::lang::RuntimeException(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      IllegalArgumentException(const IllegalArgumentException& obj) : ::java::lang::RuntimeException(obj) {}

      IllegalArgumentException();
      IllegalArgumentException(const ::java::lang::Throwable &);
      IllegalArgumentException(const ::java::lang::String &);
      IllegalArgumentException(const ::java::lang::String &, const ::java::lang::Throwable &);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(IllegalArgumentException);

    class t_IllegalArgumentException {
    public:
      PyObject_HEAD
      IllegalArgumentException object;
      static PyObject *wrap_Object(const IllegalArgumentException&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
