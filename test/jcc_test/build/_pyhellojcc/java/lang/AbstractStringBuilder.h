#ifndef java_lang_AbstractStringBuilder_H
#define java_lang_AbstractStringBuilder_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class Class;
    class StringBuffer;
    class CharSequence;
    class String;
    class Appendable;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class AbstractStringBuilder : public ::java::lang::Object {
    public:
      enum {
        mid_append_d8c6a87360a65bfc,
        mid_append_3535358b27892d62,
        mid_append_c39d10f63f3e3b62,
        mid_append_11295eaa75f99c15,
        mid_append_8c4ef90d99427fa9,
        mid_append_ba88eeceb9040dae,
        mid_append_9d36cc6d15ce04f0,
        mid_append_be91bf664544116b,
        mid_append_aff8b5c83ebbc663,
        mid_append_9611f403986e6b32,
        mid_append_8cc3a988492857d1,
        mid_append_d80ca156c78b55a7,
        mid_append_a705bf52c0fbc8a9,
        mid_appendCodePoint_be91bf664544116b,
        mid_capacity_60df5a771df5b62d,
        mid_charAt_bdde8923c8d84ea7,
        mid_codePointAt_4b23a339ec27bbb3,
        mid_codePointBefore_4b23a339ec27bbb3,
        mid_codePointCount_3d7ede988f6b3a33,
        mid_delete_7abcb35126e9515b,
        mid_deleteCharAt_be91bf664544116b,
        mid_ensureCapacity_a9395152fa63d3b0,
        mid_getChars_b97bea56ebef93e7,
        mid_indexOf_9a1fdcf5cfdf78dc,
        mid_indexOf_e65105c140eb7151,
        mid_insert_7abcb35126e9515b,
        mid_insert_a3f4844849208606,
        mid_insert_dd5bafc6d81078d1,
        mid_insert_5013578b27f5e0b8,
        mid_insert_98f82040e272d5cc,
        mid_insert_7cc7f81017d8421d,
        mid_insert_26726f0ade29aeba,
        mid_insert_21dd0287252a0684,
        mid_insert_659ccb048403f789,
        mid_insert_93a201a10165a632,
        mid_insert_9441e009188a9ce7,
        mid_insert_c39c751353502734,
        mid_lastIndexOf_9a1fdcf5cfdf78dc,
        mid_lastIndexOf_e65105c140eb7151,
        mid_length_60df5a771df5b62d,
        mid_offsetByCodePoints_3d7ede988f6b3a33,
        mid_replace_447e18418f6e038d,
        mid_reverse_3b0163deb49d372f,
        mid_setCharAt_c50c5bdc97f9afe7,
        mid_setLength_a9395152fa63d3b0,
        mid_subSequence_4648df63ce82f704,
        mid_substring_ab09aaf2e63107e3,
        mid_substring_5b238f74b18cd9ba,
        mid_toString_c041e21e63165d2d,
        mid_trimToSize_3b7a1d3d26162b85,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit AbstractStringBuilder(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      AbstractStringBuilder(const AbstractStringBuilder& obj) : ::java::lang::Object(obj) {}

      AbstractStringBuilder append(const JArray< jchar > &) const;
      AbstractStringBuilder append(jboolean) const;
      AbstractStringBuilder append(const ::java::lang::StringBuffer &) const;
      AbstractStringBuilder append(const ::java::lang::String &) const;
      AbstractStringBuilder append(const ::java::lang::CharSequence &) const;
      AbstractStringBuilder append(jdouble) const;
      AbstractStringBuilder append(jchar) const;
      AbstractStringBuilder append(jint) const;
      AbstractStringBuilder append(jlong) const;
      AbstractStringBuilder append(jfloat) const;
      AbstractStringBuilder append(const ::java::lang::Object &) const;
      AbstractStringBuilder append(const ::java::lang::CharSequence &, jint, jint) const;
      AbstractStringBuilder append(const JArray< jchar > &, jint, jint) const;
      AbstractStringBuilder appendCodePoint(jint) const;
      jint capacity() const;
      jchar charAt(jint) const;
      jint codePointAt(jint) const;
      jint codePointBefore(jint) const;
      jint codePointCount(jint, jint) const;
      AbstractStringBuilder delete$(jint, jint) const;
      AbstractStringBuilder deleteCharAt(jint) const;
      void ensureCapacity(jint) const;
      void getChars(jint, jint, const JArray< jchar > &, jint) const;
      jint indexOf(const ::java::lang::String &) const;
      jint indexOf(const ::java::lang::String &, jint) const;
      AbstractStringBuilder insert(jint, jint) const;
      AbstractStringBuilder insert(jint, jchar) const;
      AbstractStringBuilder insert(jint, jboolean) const;
      AbstractStringBuilder insert(jint, const ::java::lang::Object &) const;
      AbstractStringBuilder insert(jint, jdouble) const;
      AbstractStringBuilder insert(jint, jfloat) const;
      AbstractStringBuilder insert(jint, jlong) const;
      AbstractStringBuilder insert(jint, const ::java::lang::String &) const;
      AbstractStringBuilder insert(jint, const ::java::lang::CharSequence &) const;
      AbstractStringBuilder insert(jint, const JArray< jchar > &) const;
      AbstractStringBuilder insert(jint, const ::java::lang::CharSequence &, jint, jint) const;
      AbstractStringBuilder insert(jint, const JArray< jchar > &, jint, jint) const;
      jint lastIndexOf(const ::java::lang::String &) const;
      jint lastIndexOf(const ::java::lang::String &, jint) const;
      jint length() const;
      jint offsetByCodePoints(jint, jint) const;
      AbstractStringBuilder replace(jint, jint, const ::java::lang::String &) const;
      AbstractStringBuilder reverse() const;
      void setCharAt(jint, jchar) const;
      void setLength(jint) const;
      ::java::lang::CharSequence subSequence(jint, jint) const;
      ::java::lang::String substring(jint) const;
      ::java::lang::String substring(jint, jint) const;
      ::java::lang::String toString() const;
      void trimToSize() const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace lang {
    extern PyTypeObject PY_TYPE(AbstractStringBuilder);

    class t_AbstractStringBuilder {
    public:
      PyObject_HEAD
      AbstractStringBuilder object;
      static PyObject *wrap_Object(const AbstractStringBuilder&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
