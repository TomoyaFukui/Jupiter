#ifndef java_lang_CharSequence_H
#define java_lang_CharSequence_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class String;
    class Class;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class CharSequence : public ::java::lang::Object {
    public:
      enum {
        mid_charAt_bdde8923c8d84ea7,
        mid_length_60df5a771df5b62d,
        mid_subSequence_4648df63ce82f704,
        mid_toString_c041e21e63165d2d,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit CharSequence(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      CharSequence(const CharSequence& obj) : ::java::lang::Object(obj) {}

      jchar charAt(jint) const;
      jint length() const;
      CharSequence subSequence(jint, jint) const;
      ::java::lang::String toString() const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(CharSequence);

    class t_CharSequence {
    public:
      PyObject_HEAD
      CharSequence object;
      static PyObject *wrap_Object(const CharSequence&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
