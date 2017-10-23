#ifndef java_lang_Long_H
#define java_lang_Long_H

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

    class Long : public ::java::lang::Number {
    public:
      enum {
        mid_init$_625495ddbdca45a4,
        mid_init$_38d57a80b9fe8948,
        mid_bitCount_4a7f4b32ae8bb7df,
        mid_byteValue_51018f1683a6b595,
        mid_compare_f033cbd575b7105c,
        mid_compareTo_30a45e2465c4f803,
        mid_compareUnsigned_f033cbd575b7105c,
        mid_decode_42b4fca39337a097,
        mid_divideUnsigned_474e7493390ce6aa,
        mid_doubleValue_746fdfc2336a8dce,
        mid_equals_04e1a7382c29bc4b,
        mid_floatValue_4e51965d8682d4e7,
        mid_getLong_42b4fca39337a097,
        mid_getLong_bf939d72284a459a,
        mid_getLong_9cad517bf35ef2fe,
        mid_hashCode_60df5a771df5b62d,
        mid_hashCode_4a7f4b32ae8bb7df,
        mid_highestOneBit_260a8e55c4f9b69d,
        mid_intValue_60df5a771df5b62d,
        mid_longValue_0a482dcd1f56375a,
        mid_lowestOneBit_260a8e55c4f9b69d,
        mid_max_474e7493390ce6aa,
        mid_min_474e7493390ce6aa,
        mid_numberOfLeadingZeros_4a7f4b32ae8bb7df,
        mid_numberOfTrailingZeros_4a7f4b32ae8bb7df,
        mid_parseLong_0cbca90ccd99e162,
        mid_parseLong_1d398dbe6cfcf1c4,
        mid_parseUnsignedLong_0cbca90ccd99e162,
        mid_parseUnsignedLong_1d398dbe6cfcf1c4,
        mid_remainderUnsigned_474e7493390ce6aa,
        mid_reverse_260a8e55c4f9b69d,
        mid_reverseBytes_260a8e55c4f9b69d,
        mid_rotateLeft_f14cb9e7584956e9,
        mid_rotateRight_f14cb9e7584956e9,
        mid_shortValue_3e271dc4ae1ecc4b,
        mid_signum_4a7f4b32ae8bb7df,
        mid_sum_474e7493390ce6aa,
        mid_toBinaryString_6cc2f594436f7b3d,
        mid_toHexString_6cc2f594436f7b3d,
        mid_toOctalString_6cc2f594436f7b3d,
        mid_toString_c041e21e63165d2d,
        mid_toString_6cc2f594436f7b3d,
        mid_toString_25349188bff6632a,
        mid_toUnsignedString_6cc2f594436f7b3d,
        mid_toUnsignedString_25349188bff6632a,
        mid_valueOf_f71a75af73ce322a,
        mid_valueOf_42b4fca39337a097,
        mid_valueOf_1fe189246c742b8a,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Long(jobject obj) : ::java::lang::Number(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Long(const Long& obj) : ::java::lang::Number(obj) {}

      static jint BYTES;
      static jlong MAX_VALUE;
      static jlong MIN_VALUE;
      static jint SIZE;
      static ::java::lang::Class *TYPE;

      Long(jlong);
      Long(const ::java::lang::String &);

      static jint bitCount(jlong);
      jbyte byteValue() const;
      static jint compare(jlong, jlong);
      jint compareTo(const Long &) const;
      static jint compareUnsigned(jlong, jlong);
      static Long decode(const ::java::lang::String &);
      static jlong divideUnsigned(jlong, jlong);
      jdouble doubleValue() const;
      jboolean equals(const ::java::lang::Object &) const;
      jfloat floatValue() const;
      static Long getLong(const ::java::lang::String &);
      static Long getLong(const ::java::lang::String &, const Long &);
      static Long getLong(const ::java::lang::String &, jlong);
      jint hashCode() const;
      static jint hashCode(jlong);
      static jlong highestOneBit(jlong);
      jint intValue() const;
      jlong longValue() const;
      static jlong lowestOneBit(jlong);
      static jlong max$(jlong, jlong);
      static jlong min$(jlong, jlong);
      static jint numberOfLeadingZeros(jlong);
      static jint numberOfTrailingZeros(jlong);
      static jlong parseLong(const ::java::lang::String &);
      static jlong parseLong(const ::java::lang::String &, jint);
      static jlong parseUnsignedLong(const ::java::lang::String &);
      static jlong parseUnsignedLong(const ::java::lang::String &, jint);
      static jlong remainderUnsigned(jlong, jlong);
      static jlong reverse(jlong);
      static jlong reverseBytes(jlong);
      static jlong rotateLeft(jlong, jint);
      static jlong rotateRight(jlong, jint);
      jshort shortValue() const;
      static jint signum(jlong);
      static jlong sum(jlong, jlong);
      static ::java::lang::String toBinaryString(jlong);
      static ::java::lang::String toHexString(jlong);
      static ::java::lang::String toOctalString(jlong);
      ::java::lang::String toString() const;
      static ::java::lang::String toString(jlong);
      static ::java::lang::String toString(jlong, jint);
      static ::java::lang::String toUnsignedString(jlong);
      static ::java::lang::String toUnsignedString(jlong, jint);
      static Long valueOf(jlong);
      static Long valueOf(const ::java::lang::String &);
      static Long valueOf(const ::java::lang::String &, jint);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Long);

    class t_Long {
    public:
      PyObject_HEAD
      Long object;
      static PyObject *wrap_Object(const Long&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
