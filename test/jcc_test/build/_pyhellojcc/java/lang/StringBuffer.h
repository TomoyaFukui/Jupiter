#ifndef java_lang_StringBuffer_H
#define java_lang_StringBuffer_H

#include "java/lang/AbstractStringBuilder.h"

namespace java {
  namespace lang {
    class Class;
    class Object;
    class CharSequence;
    class String;
  }
}
template<class T> class JArray;

namespace java {
  namespace lang {

    class StringBuffer : public ::java::lang::AbstractStringBuilder {
    public:
      enum {
        mid_init$_3b7a1d3d26162b85,
        mid_init$_ff3cc5064b2f599b,
        mid_init$_38d57a80b9fe8948,
        mid_init$_a9395152fa63d3b0,
        mid_append_426fe3ac3d43fefd,
        mid_append_aa2576eef5131e53,
        mid_append_b3ba0fb122eacf19,
        mid_append_cda9f7b6e05b0a02,
        mid_append_c0c0c37c99d83c09,
        mid_append_8025af948a3e9186,
        mid_append_181a75ed6a0cb1a5,
        mid_append_cef988fbfb7d16a4,
        mid_append_84366649671152ba,
        mid_append_084bd2e5156b3c9a,
        mid_append_f43568b491d883af,
        mid_append_f41dc9a4b5104906,
        mid_append_6a37fabe21bcb893,
        mid_appendCodePoint_c0c0c37c99d83c09,
        mid_capacity_60df5a771df5b62d,
        mid_charAt_bdde8923c8d84ea7,
        mid_codePointAt_4b23a339ec27bbb3,
        mid_codePointBefore_4b23a339ec27bbb3,
        mid_codePointCount_3d7ede988f6b3a33,
        mid_delete_5dd1facc587387ac,
        mid_deleteCharAt_c0c0c37c99d83c09,
        mid_ensureCapacity_a9395152fa63d3b0,
        mid_getChars_b97bea56ebef93e7,
        mid_indexOf_9a1fdcf5cfdf78dc,
        mid_indexOf_e65105c140eb7151,
        mid_insert_6602b02ad4c6a3e5,
        mid_insert_78be8a5a60a02951,
        mid_insert_625b052e59a9dc3e,
        mid_insert_5dd1facc587387ac,
        mid_insert_5675c2755801fc25,
        mid_insert_621bb4167a4cb605,
        mid_insert_cf80aec281352ebd,
        mid_insert_094f54d4358441b9,
        mid_insert_ea8e8c239f7e298c,
        mid_insert_ac442ed20685c94e,
        mid_insert_a62abaf3a51008fb,
        mid_insert_1794229cb2a1f03c,
        mid_lastIndexOf_9a1fdcf5cfdf78dc,
        mid_lastIndexOf_e65105c140eb7151,
        mid_length_60df5a771df5b62d,
        mid_offsetByCodePoints_3d7ede988f6b3a33,
        mid_replace_c7f0aec381da8df2,
        mid_reverse_c9864812d0ad9e24,
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

      explicit StringBuffer(jobject obj) : ::java::lang::AbstractStringBuilder(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      StringBuffer(const StringBuffer& obj) : ::java::lang::AbstractStringBuilder(obj) {}

      StringBuffer();
      StringBuffer(const ::java::lang::CharSequence &);
      StringBuffer(const ::java::lang::String &);
      StringBuffer(jint);

      StringBuffer append(jfloat) const;
      StringBuffer append(jdouble) const;
      StringBuffer append(jboolean) const;
      StringBuffer append(jchar) const;
      StringBuffer append(jint) const;
      StringBuffer append(jlong) const;
      StringBuffer append(const ::java::lang::Object &) const;
      StringBuffer append(const ::java::lang::String &) const;
      StringBuffer append(const ::java::lang::CharSequence &) const;
      StringBuffer append(const JArray< jchar > &) const;
      StringBuffer append(const StringBuffer &) const;
      StringBuffer append(const ::java::lang::CharSequence &, jint, jint) const;
      StringBuffer append(const JArray< jchar > &, jint, jint) const;
      StringBuffer appendCodePoint(jint) const;
      jint capacity() const;
      jchar charAt(jint) const;
      jint codePointAt(jint) const;
      jint codePointBefore(jint) const;
      jint codePointCount(jint, jint) const;
      StringBuffer delete$(jint, jint) const;
      StringBuffer deleteCharAt(jint) const;
      void ensureCapacity(jint) const;
      void getChars(jint, jint, const JArray< jchar > &, jint) const;
      jint indexOf(const ::java::lang::String &) const;
      jint indexOf(const ::java::lang::String &, jint) const;
      StringBuffer insert(jint, const ::java::lang::CharSequence &) const;
      StringBuffer insert(jint, jboolean) const;
      StringBuffer insert(jint, jchar) const;
      StringBuffer insert(jint, jint) const;
      StringBuffer insert(jint, jfloat) const;
      StringBuffer insert(jint, jdouble) const;
      StringBuffer insert(jint, const ::java::lang::Object &) const;
      StringBuffer insert(jint, const ::java::lang::String &) const;
      StringBuffer insert(jint, const JArray< jchar > &) const;
      StringBuffer insert(jint, jlong) const;
      StringBuffer insert(jint, const ::java::lang::CharSequence &, jint, jint) const;
      StringBuffer insert(jint, const JArray< jchar > &, jint, jint) const;
      jint lastIndexOf(const ::java::lang::String &) const;
      jint lastIndexOf(const ::java::lang::String &, jint) const;
      jint length() const;
      jint offsetByCodePoints(jint, jint) const;
      StringBuffer replace(jint, jint, const ::java::lang::String &) const;
      StringBuffer reverse() const;
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
    extern PyTypeObject PY_TYPE(StringBuffer);

    class t_StringBuffer {
    public:
      PyObject_HEAD
      StringBuffer object;
      static PyObject *wrap_Object(const StringBuffer&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
