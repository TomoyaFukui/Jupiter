#ifndef java_lang_Float_H
#define java_lang_Float_H

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

    class Float : public ::java::lang::Number {
    public:
      enum {
        mid_init$_38d57a80b9fe8948,
        mid_init$_4454b3633e331cef,
        mid_init$_00f6aa63d2ba4dac,
        mid_byteValue_51018f1683a6b595,
        mid_compare_0df13f9617dc5d35,
        mid_compareTo_e492dc46818c27ee,
        mid_doubleValue_746fdfc2336a8dce,
        mid_equals_04e1a7382c29bc4b,
        mid_floatToIntBits_4b148a9e1a682ecf,
        mid_floatToRawIntBits_4b148a9e1a682ecf,
        mid_floatValue_4e51965d8682d4e7,
        mid_hashCode_60df5a771df5b62d,
        mid_hashCode_4b148a9e1a682ecf,
        mid_intBitsToFloat_8c1eea33f02c2c30,
        mid_intValue_60df5a771df5b62d,
        mid_isFinite_ed9bbe984b7c6385,
        mid_isInfinite_318f7cae9d6a33e6,
        mid_isInfinite_ed9bbe984b7c6385,
        mid_isNaN_318f7cae9d6a33e6,
        mid_isNaN_ed9bbe984b7c6385,
        mid_longValue_0a482dcd1f56375a,
        mid_max_6b6277a645ad3dea,
        mid_min_6b6277a645ad3dea,
        mid_parseFloat_b146d86f2dc2ae35,
        mid_shortValue_3e271dc4ae1ecc4b,
        mid_sum_6b6277a645ad3dea,
        mid_toHexString_3ef4f0a5c27c2560,
        mid_toString_c041e21e63165d2d,
        mid_toString_3ef4f0a5c27c2560,
        mid_valueOf_aba530a5b0b9f932,
        mid_valueOf_cccf8ad87309d98e,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Float(jobject obj) : ::java::lang::Number(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Float(const Float& obj) : ::java::lang::Number(obj) {}

      static jint BYTES;
      static jint MAX_EXPONENT;
      static jfloat MAX_VALUE;
      static jint MIN_EXPONENT;
      static jfloat MIN_NORMAL;
      static jfloat MIN_VALUE;
      static jfloat NEGATIVE_INFINITY;
      static jfloat NaN;
      static jfloat POSITIVE_INFINITY;
      static jint SIZE;
      static ::java::lang::Class *TYPE;

      Float(const ::java::lang::String &);
      Float(jdouble);
      Float(jfloat);

      jbyte byteValue() const;
      static jint compare(jfloat, jfloat);
      jint compareTo(const Float &) const;
      jdouble doubleValue() const;
      jboolean equals(const ::java::lang::Object &) const;
      static jint floatToIntBits(jfloat);
      static jint floatToRawIntBits(jfloat);
      jfloat floatValue() const;
      jint hashCode() const;
      static jint hashCode(jfloat);
      static jfloat intBitsToFloat(jint);
      jint intValue() const;
      static jboolean isFinite(jfloat);
      jboolean isInfinite() const;
      static jboolean isInfinite(jfloat);
      jboolean isNaN() const;
      static jboolean isNaN(jfloat);
      jlong longValue() const;
      static jfloat max$(jfloat, jfloat);
      static jfloat min$(jfloat, jfloat);
      static jfloat parseFloat(const ::java::lang::String &);
      jshort shortValue() const;
      static jfloat sum(jfloat, jfloat);
      static ::java::lang::String toHexString(jfloat);
      ::java::lang::String toString() const;
      static ::java::lang::String toString(jfloat);
      static Float valueOf(jfloat);
      static Float valueOf(const ::java::lang::String &);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Float);

    class t_Float {
    public:
      PyObject_HEAD
      Float object;
      static PyObject *wrap_Object(const Float&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
