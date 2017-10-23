#ifndef java_lang_Comparable_H
#define java_lang_Comparable_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class Class;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Comparable : public ::java::lang::Object {
    public:
      enum {
        mid_compareTo_158021391988ca97,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Comparable(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Comparable(const Comparable& obj) : ::java::lang::Object(obj) {}

      jint compareTo(const ::java::lang::Object &) const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Comparable);

    class t_Comparable {
    public:
      PyObject_HEAD
      Comparable object;
      PyTypeObject *parameters[1];
      static PyTypeObject **parameters_(t_Comparable *self)
      {
        return (PyTypeObject **) &(self->parameters);
      }
      static PyObject *wrap_Object(const Comparable&);
      static PyObject *wrap_jobject(const jobject&);
      static PyObject *wrap_Object(const Comparable&, PyTypeObject *);
      static PyObject *wrap_jobject(const jobject&, PyTypeObject *);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
