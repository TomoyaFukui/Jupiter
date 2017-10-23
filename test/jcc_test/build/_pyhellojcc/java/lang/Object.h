#ifndef java_lang_Object_H
#define java_lang_Object_H

#include "JObject.h"

namespace java {
  namespace lang {
    class InterruptedException;
    class String;
    class Class;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Object : public JObject {
    public:
      enum {
        mid_init$_3b7a1d3d26162b85,
        mid_equals_04e1a7382c29bc4b,
        mid_getClass_0922d10264375499,
        mid_hashCode_60df5a771df5b62d,
        mid_notify_3b7a1d3d26162b85,
        mid_notifyAll_3b7a1d3d26162b85,
        mid_toString_c041e21e63165d2d,
        mid_wait_3b7a1d3d26162b85,
        mid_wait_625495ddbdca45a4,
        mid_wait_8427b8c20e0848b6,
        mid_finalize_3b7a1d3d26162b85,
        mid_clone_6a490f1da80a3003,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Object(jobject obj) : ::JObject(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Object(const Object& obj) : ::JObject(obj) {}

      Object();

      jboolean equals(const Object &) const;
      ::java::lang::Class getClass() const;
      jint hashCode() const;
      void notify() const;
      void notifyAll() const;
      ::java::lang::String toString() const;
      void wait() const;
      void wait(jlong) const;
      void wait(jlong, jint) const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Object);

    class t_Object {
    public:
      PyObject_HEAD
      Object object;
      static PyObject *wrap_Object(const Object&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
