#ifndef java_lang_Appendable_H
#define java_lang_Appendable_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class CharSequence;
    class Class;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Appendable : public ::java::lang::Object {
    public:
      enum {
        mid_append_3108d4be035ceaa2,
        mid_append_e2ee5ed460890580,
        mid_append_be35c96e4bf84f5f,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Appendable(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Appendable(const Appendable& obj) : ::java::lang::Object(obj) {}

      Appendable append(const ::java::lang::CharSequence &) const;
      Appendable append(jchar) const;
      Appendable append(const ::java::lang::CharSequence &, jint, jint) const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Appendable);

    class t_Appendable {
    public:
      PyObject_HEAD
      Appendable object;
      static PyObject *wrap_Object(const Appendable&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
