#ifndef java_lang_RuntimeException_H
#define java_lang_RuntimeException_H

#include "java/lang/Exception.h"

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

    class RuntimeException : public ::java::lang::Exception {
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

      explicit RuntimeException(jobject obj) : ::java::lang::Exception(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      RuntimeException(const RuntimeException& obj) : ::java::lang::Exception(obj) {}

      RuntimeException();
      RuntimeException(const ::java::lang::Throwable &);
      RuntimeException(const ::java::lang::String &);
      RuntimeException(const ::java::lang::String &, const ::java::lang::Throwable &);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(RuntimeException);

    class t_RuntimeException {
    public:
      PyObject_HEAD
      RuntimeException object;
      static PyObject *wrap_Object(const RuntimeException&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
