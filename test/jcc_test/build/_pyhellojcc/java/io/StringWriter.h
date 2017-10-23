#ifndef java_io_StringWriter_H
#define java_io_StringWriter_H

#include "java/io/Writer.h"

namespace java {
  namespace lang {
    class Class;
    class StringBuffer;
    class CharSequence;
    class String;
  }
}
template<class T> class JArray;

namespace java {
  namespace io {

    class StringWriter : public ::java::io::Writer {
    public:
      enum {
        mid_init$_3b7a1d3d26162b85,
        mid_init$_a9395152fa63d3b0,
        mid_append_a6909a6e91f34e5c,
        mid_append_dc0be884298a28b7,
        mid_append_c9c6d796987b0032,
        mid_close_3b7a1d3d26162b85,
        mid_flush_3b7a1d3d26162b85,
        mid_getBuffer_c9864812d0ad9e24,
        mid_toString_c041e21e63165d2d,
        mid_write_38d57a80b9fe8948,
        mid_write_a9395152fa63d3b0,
        mid_write_328bb6dd18104856,
        mid_write_7b7b455231dae263,
        max_mid
      };

      static ::java::lang::Class *class$;
      static jmethodID *mids$;
      static bool live$;
      static jclass initializeClass(bool);

      explicit StringWriter(jobject obj) : ::java::io::Writer(obj) {
        if (obj != NULL)
          env->getClass(initializeClass);
      }
      StringWriter(const StringWriter& obj) : ::java::io::Writer(obj) {}

      StringWriter();
      StringWriter(jint);

      StringWriter append(jchar) const;
      StringWriter append(const ::java::lang::CharSequence &) const;
      StringWriter append(const ::java::lang::CharSequence &, jint, jint) const;
      void close() const;
      void flush() const;
      ::java::lang::StringBuffer getBuffer() const;
      ::java::lang::String toString() const;
      void write(const ::java::lang::String &) const;
      void write(jint) const;
      void write(const ::java::lang::String &, jint, jint) const;
      void write(const JArray< jchar > &, jint, jint) const;
    };
  }
}

#include <Python.h>

namespace java {
  namespace io {
    extern PyTypeObject PY_TYPE(StringWriter);

    class t_StringWriter {
    public:
      PyObject_HEAD
      StringWriter object;
      static PyObject *wrap_Object(const StringWriter&);
      static PyObject *wrap_jobject(const jobject&);
      static void install(PyObject *module);
      static void initialize(PyObject *module);
    };
  }
}

#endif
