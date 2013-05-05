/* -*- C -*- ***********************************************
Copyright (c) 2000, BeOpen.com.
Copyright (c) 1995-2000, Corporation for National Research Initiatives.
Copyright (c) 1990-1995, Stichting Mathematisch Centrum.
All rights reserved.

See the file "Misc/COPYRIGHT" for information on usage and
redistribution of this file, and for a DISCLAIMER OF ALL WARRANTIES.
******************************************************************/

/* Module configuration */

/* !!! !!! !!! This file is edited by the makesetup script !!! !!! !!! */

/* This file contains the table of built-in modules.
   See init_builtin() in import.c. */

#include "Python.h"

#ifdef __cplusplus
extern "C" {
#endif


/* -- ADDMODULE MARKER 1 -- */
extern void init_bisect(void);
extern void init_codecs(void);
extern void init_collections(void);
extern void init_functools(void);
extern void init_hashlib(void);
extern void init_locale(void);
extern void init_random(void);
extern void init_socket(void);
extern void init_sre(void);
extern void init_ssl(void);
extern void init_struct(void);
extern void init_weakref(void);
extern void initarray(void);
extern void initbinascii(void);
extern void initcPickle(void);
extern void initcStringIO(void);
extern void initerrno(void);
extern void initfcntl(void);
extern void initgc(void);
extern void initgrp(void);
extern void initimp(void);
extern void inititertools(void);
extern void initmath(void);
extern void initoperator(void);
extern void initposix(void);
extern void initpwd(void);
extern void initselect(void);
extern void initsignal(void);
extern void initstrop(void);
extern void initthread(void);
extern void inittime(void);
extern void initzipimport(void);
extern void initzlib(void);

extern void PyMarshal_Init(void);
extern void initimp(void);
extern void initgc(void);
extern void init_ast(void);
extern void _PyWarnings_Init(void);

struct _inittab _PyImport_Inittab[] = {

/* -- ADDMODULE MARKER 2 -- */
	{"_bisect", init_bisect},
	{"_codecs", init_codecs},
	{"_collections", init_collections},
	{"_functools", init_functools},
	{"_hashlib", init_hashlib},
	{"_locale", init_locale},
	{"_random", init_random},
	{"_socket", init_socket},
	{"_sre", init_sre},
	{"_ssl", init_ssl},
	{"_struct", init_struct},
	{"_weakref", init_weakref},
	{"array", initarray},
	{"binascii", initbinascii},
	{"cPickle", initcPickle},
	{"cStringIO", initcStringIO},
	{"errno", initerrno},
	{"fcntl", initfcntl},
	{"gc", initgc},
	{"grp", initgrp},
	{"imp", initimp},
	{"itertools", inititertools},
	{"math", initmath},
	{"operator", initoperator},
	{"posix", initposix},
	{"pwd", initpwd},
	{"select", initselect},
	{"signal", initsignal},
	{"strop", initstrop},
	{"thread", initthread},
	{"time", inittime},
	{"zipimport", initzipimport},
	{"zlib", initzlib},

    /* This module lives in marshal.c */
    {"marshal", PyMarshal_Init},

    /* This lives in import.c */
    {"imp", initimp},

    /* This lives in Python/Python-ast.c */
    {"_ast", init_ast},

    /* These entries are here for sys.builtin_module_names */
    {"__main__", NULL},
    {"__builtin__", NULL},
    {"sys", NULL},
    {"exceptions", NULL},

    /* This lives in gcmodule.c */
    {"gc", initgc},

    /* This lives in _warnings.c */
    {"_warnings", _PyWarnings_Init},

    /* Sentinel */
    {0, 0}
};


#ifdef __cplusplus
}
#endif
