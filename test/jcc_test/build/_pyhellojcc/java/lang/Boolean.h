#ifndef java_lang_Boolean_H
#define java_lang_Boolean_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class Class;
    class Comparable;
    class String;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Boolean : public ::java::lang::Object {
    public:
      enum {
        mid_init$_4e7a2bdefbe801b3,
        mid_init$_38d57a80b9fe8948,
        mid_booleanValue_318f7cae9d6a33e6,
        mid_compare_dafedceba9ed4732,
        mid_compareTo_2782815c9d802298,
        mid_equals_04e1a7382c29bc4b,
        mid_getBoolean_1dfa664233a47103,
        mid_hashCode_60df5a771df5b62d,
        mid_hashCode_25b517ea402753ea,
        mid_logicalAnd_38d082b5ba57e3da,
        mid_logicalOr_38d082b5ba57e3da,
        mid_logicalXor_38d082b5ba57e3da,
        mid_parseBoolean_1dfa664233a47103,
        mid_toString_c041e21e63165d2d,
        mid_toString_ea6d2a082bd69826,
        mid_valueOf_b199b80b8fd38ec9,
        mid_valueOf_3abd42eab99f6729,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Boolean(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Boolean(const Boolean& obj) : ::java::lang::Object(obj) {}

      static Boolean *FALSE;
      static Boolean *TRUE;
      static ::java::lang::Class *TYPE;

      Boolean(jboolean);
      Boolean(const ::java::lang::String &);

      jboolean booleanValue() const;
      static jint compare(jboolean, jboolean);
      jint compareTo(const Boolean &) const;
      jboolean equals(const ::java::lang::Object &) const;
      static jboolean getBoolean(const ::java::lang::String &);
      jint hashCode() const;
      static jint hashCode(jboolean);
      static jboolean logicalAnd(jboolean, jboolean);
      static jboolean logicalOr(jboolean, jboolean);
      static jboolean logicalXor(jboolean, jboolean);
      static jboolean parseBoolean(const ::java::lang::String &);
      ::java::lang::String toString() const;
      static ::java::lang::String toString(jboolean);
      static Boolean valueOf(const ::java::lang::String &);
      static Boolean valueOf(jboolean);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Boolean);

    class t_Boolean {
    public:
      PyObject_HEAD
      Boolean object;
      static PyObject *wrap_Object(const Boolean&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
