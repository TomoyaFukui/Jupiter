#ifndef java_lang_Throwable_H
#define java_lang_Throwable_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class Class;
    class StackTraceElement;
    class String;
  }
  namespace io {
    class PrintWriter;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Throwable : public ::java::lang::Object {
    public:
      enum {
        mid_init$_3b7a1d3d26162b85,
        mid_init$_38d57a80b9fe8948,
        mid_init$_5df017320dfbf543,
        mid_addSuppressed_359aa6a1d41f0219,
        mid_fillInStackTrace_81fe1f12b87f141b,
        mid_getCause_81fe1f12b87f141b,
        mid_getLocalizedMessage_c041e21e63165d2d,
        mid_getMessage_c041e21e63165d2d,
        mid_getStackTrace_c4e857717549de1a,
        mid_getSuppressed_58ff4eb97ed3fe96,
        mid_initCause_bcdf3ac5798fea3a,
        mid_printStackTrace_3b7a1d3d26162b85,
        mid_printStackTrace_d60231ec0f744a70,
        mid_setStackTrace_5e3c0689cd8db190,
        mid_toString_c041e21e63165d2d,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Throwable(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Throwable(const Throwable& obj) : ::java::lang::Object(obj) {}

      Throwable();
      Throwable(const ::java::lang::String &);
      Throwable(const ::java::lang::String &, const Throwable &);

      void addSuppressed(const Throwable &) const;
      Throwable fillInStackTrace() const;
      Throwable getCause() const;
      ::java::lang::String getLocalizedMessage() const;
      ::java::lang::String getMessage() const;
      JArray< ::java::lang::StackTraceElement > getStackTrace() const;
      JArray< Throwable > getSuppressed() const;
      Throwable initCause(const Throwable &) const;
      void printStackTrace() const;
      void printStackTrace(const ::java::io::PrintWriter &) const;
      void setStackTrace(const JArray< ::java::lang::StackTraceElement > &) const;
      ::java::lang::String toString() const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Throwable);

    class t_Throwable {
    public:
      PyObject_HEAD
      Throwable object;
      static PyObject *wrap_Object(const Throwable&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
