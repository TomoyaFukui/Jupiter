#ifndef java_lang_Exception_H
#define java_lang_Exception_H

#include "java/lang/Throwable.h"

namespace java {
  namespace lang {
    class String;
    class Class;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Exception : public ::java::lang::Throwable {
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

      explicit Exception(jobject obj) : ::java::lang::Throwable(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Exception(const Exception& obj) : ::java::lang::Throwable(obj) {}

      Exception();
      Exception(const ::java::lang::Throwable &);
      Exception(const ::java::lang::String &);
      Exception(const ::java::lang::String &, const ::java::lang::Throwable &);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Exception);

    class t_Exception {
    public:
      PyObject_HEAD
      Exception object;
      static PyObject *wrap_Object(const Exception&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
