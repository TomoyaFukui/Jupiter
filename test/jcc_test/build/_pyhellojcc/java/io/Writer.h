#ifndef java_io_Writer_H
#define java_io_Writer_H

#include "java/lang/Object.h"

namespace java {
  namespace lang {
    class Class;
    class CharSequence;
    class String;
    class Appendable;
  }
}
template<class T> class JArray;

namespace java {
  namespace io {

    class Writer : public ::java::lang::Object {
    public:
      enum {
        mid_append_49eef9361d8e81fe,
        mid_append_2053018ad2e0ce58,
        mid_append_911f2ada89edf868,
        mid_close_3b7a1d3d26162b85,
        mid_flush_3b7a1d3d26162b85,
        mid_write_ee30b01cc5d9d615,
        mid_write_a9395152fa63d3b0,
        mid_write_38d57a80b9fe8948,
        mid_write_7b7b455231dae263,
        mid_write_328bb6dd18104856,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit Writer(jobject obj) : ::java::lang::Object(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      Writer(const Writer& obj) : ::java::lang::Object(obj) {}

      Writer append(jchar) const;
      Writer append(const ::java::lang::CharSequence &) const;
      Writer append(const ::java::lang::CharSequence &, jint, jint) const;
      void close() const;
      void flush() const;
      void write(const JArray< jchar > &) const;
      void write(jint) const;
      void write(const ::java::lang::String &) const;
      void write(const JArray< jchar > &, jint, jint) const;
      void write(const ::java::lang::String &, jint, jint) const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace io {
    extern PyTypeObject PY_TYPE(Writer);

    class t_Writer {
    public:
      PyObject_HEAD
      Writer object;
      static PyObject *wrap_Object(const Writer&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
