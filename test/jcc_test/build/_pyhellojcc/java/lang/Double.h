#ifndef java_lang_Double_H
#define java_lang_Double_H

#include "java/lang/Number.h"

namespace java {
  namespace lang {
    class Class;
    class Comparable;
    class Object;
    class NumberFormatException;
    class String;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class Double : public ::java::lang::Number {
    public:
      enum {
        mid_init$_4454b3633e331cef,
        mid_init$_38d57a80b9fe8948,
        mid_byteValue_51018f1683a6b595,
        mid_compare_6839564546e9f1fc,
        mid_compareTo_92f4a8554f58faae,
        mid_doubleToLongBits_1c49831d725774c8,
        mid_doubleToRawLongBits_1c49831d725774c8,
        mid_doubleValue_746fdfc2336a8dce,
        mid_equals_04e1a7382c29bc4b,
        mid_floatValue_4e51965d8682d4e7,
        mid_hashCode_60df5a771df5b62d,
        mid_hashCode_d2deb6bff94c033f,
        mid_intValue_60df5a771df5b62d,
        mid_isFinite_cd546b9f1e12b4df,
        mid_isInfinite_318f7cae9d6a33e6,
        mid_isInfinite_cd546b9f1e12b4df,
        mid_isNaN_318f7cae9d6a33e6,
        mid_isNaN_cd546b9f1e12b4df,
        mid_longBitsToDouble_44c28eee86f9cf15,
        mid_longValue_0a482dcd1f56375a,
        mid_max_e2d05d76088434f9,
        mid_min_e2d05d76088434f9,
        mid_parseDouble_28e2edb6c5cc6da0,
        mid_shortValue_3e271dc4ae1ecc4b,
        mid_sum_e2d05d76088434f9,
        mid_toHexString_7d2d6127fa523a6f,
        mid_toString_c041e21e63165d2d,
        mid_toString_7d2d6127fa523a6f,
        mid_valueOf_287134074f47287d,
        mid_valueOf_29fd566b4ddeb2ed,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Double(jobject obj) : ::java::lang::Number(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Double(const Double& obj) : ::java::lang::Number(obj) {}

      static jint BYTES;
      static jint MAX_EXPONENT;
      static jdouble MAX_VALUE;
      static jint MIN_EXPONENT;
      static jdouble MIN_NORMAL;
      static jdouble MIN_VALUE;
      static jdouble NEGATIVE_INFINITY;
      static jdouble NaN;
      static jdouble POSITIVE_INFINITY;
      static jint SIZE;
      static ::java::lang::Class *TYPE;

      Double(jdouble);
      Double(const ::java::lang::String &);

      jbyte byteValue() const;
      static jint compare(jdouble, jdouble);
      jint compareTo(const Double &) const;
      static jlong doubleToLongBits(jdouble);
      static jlong doubleToRawLongBits(jdouble);
      jdouble doubleValue() const;
      jboolean equals(const ::java::lang::Object &) const;
      jfloat floatValue() const;
      jint hashCode() const;
      static jint hashCode(jdouble);
      jint intValue() const;
      static jboolean isFinite(jdouble);
      jboolean isInfinite() const;
      static jboolean isInfinite(jdouble);
      jboolean isNaN() const;
      static jboolean isNaN(jdouble);
      static jdouble longBitsToDouble(jlong);
      jlong longValue() const;
      static jdouble max$(jdouble, jdouble);
      static jdouble min$(jdouble, jdouble);
      static jdouble parseDouble(const ::java::lang::String &);
      jshort shortValue() const;
      static jdouble sum(jdouble, jdouble);
      static ::java::lang::String toHexString(jdouble);
      ::java::lang::String toString() const;
      static ::java::lang::String toString(jdouble);
      static Double valueOf(const ::java::lang::String &);
      static Double valueOf(jdouble);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Double);

    class t_Double {
    public:
      PyObject_HEAD
      Double object;
      static PyObject *wrap_Object(const Double&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
