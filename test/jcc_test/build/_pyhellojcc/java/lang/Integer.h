#ifndef java_lang_Integer_H
#define java_lang_Integer_H

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

    class Integer : public ::java::lang::Number {
    public:
      enum {
        mid_init$_a9395152fa63d3b0,
        mid_init$_38d57a80b9fe8948,
        mid_bitCount_4b23a339ec27bbb3,
        mid_byteValue_51018f1683a6b595,
        mid_compare_3d7ede988f6b3a33,
        mid_compareTo_f87645181f9a1291,
        mid_compareUnsigned_3d7ede988f6b3a33,
        mid_decode_12066d8742764eab,
        mid_divideUnsigned_3d7ede988f6b3a33,
        mid_doubleValue_746fdfc2336a8dce,
        mid_equals_04e1a7382c29bc4b,
        mid_floatValue_4e51965d8682d4e7,
        mid_getInteger_12066d8742764eab,
        mid_getInteger_1eeab593d705129b,
        mid_getInteger_43f55f4841c44178,
        mid_hashCode_60df5a771df5b62d,
        mid_hashCode_4b23a339ec27bbb3,
        mid_highestOneBit_4b23a339ec27bbb3,
        mid_intValue_60df5a771df5b62d,
        mid_longValue_0a482dcd1f56375a,
        mid_lowestOneBit_4b23a339ec27bbb3,
        mid_max_3d7ede988f6b3a33,
        mid_min_3d7ede988f6b3a33,
        mid_numberOfLeadingZeros_4b23a339ec27bbb3,
        mid_numberOfTrailingZeros_4b23a339ec27bbb3,
        mid_parseInt_9a1fdcf5cfdf78dc,
        mid_parseInt_e65105c140eb7151,
        mid_parseUnsignedInt_9a1fdcf5cfdf78dc,
        mid_parseUnsignedInt_e65105c140eb7151,
        mid_remainderUnsigned_3d7ede988f6b3a33,
        mid_reverse_4b23a339ec27bbb3,
        mid_reverseBytes_4b23a339ec27bbb3,
        mid_rotateLeft_3d7ede988f6b3a33,
        mid_rotateRight_3d7ede988f6b3a33,
        mid_shortValue_3e271dc4ae1ecc4b,
        mid_signum_4b23a339ec27bbb3,
        mid_sum_3d7ede988f6b3a33,
        mid_toBinaryString_ab09aaf2e63107e3,
        mid_toHexString_ab09aaf2e63107e3,
        mid_toOctalString_ab09aaf2e63107e3,
        mid_toString_c041e21e63165d2d,
        mid_toString_ab09aaf2e63107e3,
        mid_toString_5b238f74b18cd9ba,
        mid_toUnsignedLong_dcd2935a5563d052,
        mid_toUnsignedString_ab09aaf2e63107e3,
        mid_toUnsignedString_5b238f74b18cd9ba,
        mid_valueOf_6e6e43bd124aa371,
        mid_valueOf_12066d8742764eab,
        mid_valueOf_1eeab593d705129b,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Integer(jobject obj) : ::java::lang::Number(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Integer(const Integer& obj) : ::java::lang::Number(obj) {}

      static jint BYTES;
      static jint MAX_VALUE;
      static jint MIN_VALUE;
      static jint SIZE;
      static ::java::lang::Class *TYPE;

      Integer(jint);
      Integer(const ::java::lang::String &);

      static jint bitCount(jint);
      jbyte byteValue() const;
      static jint compare(jint, jint);
      jint compareTo(const Integer &) const;
      static jint compareUnsigned(jint, jint);
      static Integer decode(const ::java::lang::String &);
      static jint divideUnsigned(jint, jint);
      jdouble doubleValue() const;
      jboolean equals(const ::java::lang::Object &) const;
      jfloat floatValue() const;
      static Integer getInteger(const ::java::lang::String &);
      static Integer getInteger(const ::java::lang::String &, jint);
      static Integer getInteger(const ::java::lang::String &, const Integer &);
      jint hashCode() const;
      static jint hashCode(jint);
      static jint highestOneBit(jint);
      jint intValue() const;
      jlong longValue() const;
      static jint lowestOneBit(jint);
      static jint max$(jint, jint);
      static jint min$(jint, jint);
      static jint numberOfLeadingZeros(jint);
      static jint numberOfTrailingZeros(jint);
      static jint parseInt(const ::java::lang::String &);
      static jint parseInt(const ::java::lang::String &, jint);
      static jint parseUnsignedInt(const ::java::lang::String &);
      static jint parseUnsignedInt(const ::java::lang::String &, jint);
      static jint remainderUnsigned(jint, jint);
      static jint reverse(jint);
      static jint reverseBytes(jint);
      static jint rotateLeft(jint, jint);
      static jint rotateRight(jint, jint);
      jshort shortValue() const;
      static jint signum(jint);
      static jint sum(jint, jint);
      static ::java::lang::String toBinaryString(jint);
      static ::java::lang::String toHexString(jint);
      static ::java::lang::String toOctalString(jint);
      ::java::lang::String toString() const;
      static ::java::lang::String toString(jint);
      static ::java::lang::String toString(jint, jint);
      static jlong toUnsignedLong(jint);
      static ::java::lang::String toUnsignedString(jint);
      static ::java::lang::String toUnsignedString(jint, jint);
      static Integer valueOf(jint);
      static Integer valueOf(const ::java::lang::String &);
      static Integer valueOf(const ::java::lang::String &, jint);
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(Integer);

    class t_Integer {
    public:
      PyObject_HEAD
      Integer object;
      static PyObject *wrap_Object(const Integer&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
