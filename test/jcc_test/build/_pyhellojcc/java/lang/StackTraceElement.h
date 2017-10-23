#ifndef java_lang_StackTraceElement_H
#define java_lang_StackTraceElement_H

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

    class StackTraceElement : public ::java::lang::Object {
    public:
      enum {
        mid_init$_1a58a3c5e13d2312,
        mid_equals_04e1a7382c29bc4b,
        mid_getClassName_c041e21e63165d2d,
        mid_getFileName_c041e21e63165d2d,
        mid_getLineNumber_60df5a771df5b62d,
        mid_getMethodName_c041e21e63165d2d,
        mid_hashCode_60df5a771df5b62d,
        mid_isNativeMethod_318f7cae9d6a33e6,
        mid_toString_c041e21e63165d2d,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit StackTraceElement(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      StackTraceElement(const StackTraceElement& obj) : ::java::lang::Object(obj) {}

      StackTraceElement(const ::java::lang::String &, const ::java::lang::String &, const ::java::lang::String &, jint);

      jboolean equals(const ::java::lang::Object &) const;
      ::java::lang::String getClassName() const;
      ::java::lang::String getFileName() const;
      jint getLineNumber() const;
      ::java::lang::String getMethodName() const;
      jint hashCode() const;
      jboolean isNativeMethod() const;
      ::java::lang::String toString() const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(StackTraceElement);

    class t_StackTraceElement {
    public:
      PyObject_HEAD
      StackTraceElement object;
      static PyObject *wrap_Object(const StackTraceElement&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
