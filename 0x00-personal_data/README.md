0x00-personal_data

Learning resources:
    What Is PII, non-PII, and Personal Data?
    logging documentation
    bcrypt package
    Logging to Files, Setting Levels, and Formatting

Learning objectives:
    Examples of Personally Identifiable Information (PII)
    How to implement a log filter that will obfuscate PII fields
    How to encrypt a password and check the validity of an input password
    How to authenticate to a database using environment variables

Key concepts, functions etc:
    PII, non-PII, and Personal Data:

    logging:
        flexible event logging system for applications and libraries
        import logging, import mylib, logger = logging.getLogger(__name__), logging.basicConfig(), logger.info(), logger.info(),  basicConfig(), logging.getLogger(name), getLogger()

        class logging.Logger, name, getLogger(), level, setLevel(), parent, propagate, logging.getLogger().error()

        handlers, addHandler(), removeHandler()

        disabled
        
        setLevel(level), NOTSET, WARNING, INFO, getEffectiveLevel(), isEnabledFor()

        isEnabledFor(level), logging.disable(level)

        getEffectiveLevel(), NOTSET, setLevel(), logging.DEBUG, logging.INFO etc.

        getChild(suffix), logging.getLogger().getChild(), logging.getLogger()

        getChildren(), logging.getLogger().getChildren()

        debug(msg, *args, **kwargs), sys.exc_info(), LogRecord, Formatter, Logger.propagate, lastResort

        info(msg, *args, **kwargs), INFO, debug()

        warning(msg, *args, **kwargs), WARNING, debug()

        error(msg, *args, **kwargs), ERROR, debug()

        critical(msg, *args, **kwargs), CRITICAL, debug()

        log(level, msg, *args, **kwargs), debug()

        exception(msg, *args, **kwargs), ERROR, debug()

        addFilter(filter)

        removeFilter(filter)

        filter(record), addHandler(hdlr), removeHandler(hdlr)

        findCaller(stack_info=False, stacklevel=1), debug()

        handle(record), filter()

        makeRecord(name, level, fn, lno, msg, args, exc_info, func=None, extra=None, sinfo=None), LogRecord instances

    Logging Levels:
        logging.NOTSET, logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL

    Handler Objects:
        Handler.__init__()
        class logging.Handler:
            __init__(level=NOTSET), Handler, createLock()
            createLock(), acquire(), release(), setFormatter(fmt), addFilter(filter), removeFilter(filter), filter(record), flush(), handle(record), format(record0
            setLevel(Level), NOTSET, INFO
            close(), shutdown()
            handleError(record), emit(), raiseExceptions
            emit(record), NotImplementedError
            logging.handlers

    Formatter Objects:
        class logging.Formatter(fmt=None, datefmt=None, style='%', validate=True, *, defaults=None):
            format(record), asctime, formatTime(), formatException(), Formatter, formatStack()
            formatTime(record, datefmt=None), format(), time.strftime(), time.localtime(), time.gmtime()
            formatException(exc_info), sys.exc_info(), traceback.print_exception()
            formatStack(stack_info), traceback.print_stack()

        class logging.BufferingFormatter(linefmt=None):
            formatHeader(records), formatFooter(records), format(records)

    Filter Objects
        Filters can be used by Handlers and Loggers
        class logging.Filter(name=''):
            filter(record), debug(), info(), filter(), LogRecord, Handler

    LogRecord Objects
        LogRecord, Logger, makeLogRecord()
        class logging.LogRecord(name, level, pathname, lineno, msg, args, exc_info, func=None, sinfo=None):
            getMessage(), LogRecord, str(), getLogRecordFactory(), setLogRecordFactory() 

    LogRecord attributes
        str.format(), string.Template, {attrname}

    LoggerAdapter Objects
        class logging.LoggerAdapter(logger, extra):
            process(msg, kwargs), manager, _log

    Thread Safety
        signal, threading

    Module-Level Functions
        logging.getLogger(name=None)
        logging.getLoggerClass(), Logger, setLoggerClass(), class MyLogger(logging.getLoggerClass()):
            logging.getLogRecordFactory(), LogRecord, setLogRecordFactory()
            logging.debug(msg, *args, **kwargs), Logger.debug(), basicConfig()
            logging.info(msg, *args, **kwargs), INFO, debug()
            logging.warning(msg, *args, **kwargs), WARNING, debug()
            logging.error(msg, *args, **kwargs), ERROR, debug()
            logging.critical(msg, *args, **kwargs), CRITICAL, debug()
            logging.exception(msg, *args, **kwargs), ERROR, debug()
            logging.log(level, msg, *args, **kwargs), debug()
            logging.disable(level=CRITICAL), logging.disable(logging.NOTSET)
            logging.addLevelName(level, levelName), Formatter
            logging.getLevelNamesMapping(), CRITICAL
            logging.getLevelName(level), CRITICAL, ERROR, WARNING, INFO or DEBUG, addLevelName()
            logging.getHandlerByName(name)
            logging.getHandlerNames()
            logging.makeLogRecord(attrdict), LogRecord
            logging.basicConfig(**kwargs), StreamHandler, Formatter, debug(), info(), warning(), error(), critical(), basicConfig()
            logging.shutdown(), atexit
            logging.setLoggerClass(klass), __Init__(), logging.getLogger()
            logging.setLogRecordFactory(factory), LogRecord, getLogRecordFactory()
            factory(name, level, fn, lno, msg, args, exc_info, func=None, sinfo=None, **kwargs)

    Module-Level Attributes
        logging.lastResort, StreamHandler, sys.stderr, WARNING, lastResort
        logging.raiseExceptions, raiseExceptions

    Integration with the warnings module
        captureWarnings(), logging, warnings
        logging.captureWarnings(capture), warnings, warnings.formatwarning(), WARNING

bcrypt:
    Acceptable password hashing for your software and your servers (but you should really use argon2id or scrypt)

    Password Hashing:
        Hashing and then later checking that a password matches the previous hashed password is very simple:

        >>> import bcrypt
        >>> password = b"super secret password"
        >>> # Hash a password for the first time, with a randomly-generated salt
        >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt())
        >>> # Check that an unhashed password matches one that has previously been
        >>> # hashed
        >>> if bcrypt.checkpw(password, hashed):
        ...     print("It Matches!")
        ... else:
        ...     print("It Does not Match :(")

    KDF:
        As of 3.0.0 bcrypt now offers a kdf function which does bcrypt_pbkdf. This KDF is used in OpenSSH's newer encrypted private key format.

        >>> import bcrypt
        >>> key = bcrypt.kdf(
        ...     password=b'password',
        ...     salt=b'salt',
        ...     desired_key_bytes=32,
        ...     rounds=100)

    Adjustable Work Factor:
        One of bcrypt's features is an adjustable logarithmic work factor. To adjust the work factor merely pass the desired number of rounds to bcrypt.gensalt(rounds=12) which defaults to 12):

        >>> import bcrypt
        >>> password = b"super secret password"
        >>> # Hash a password for the first time, with a certain number of rounds
        >>> hashed = bcrypt.hashpw(password, bcrypt.gensalt(14))
        >>> # Check that a unhashed password matches one that has previously been
        >>> #   hashed
        >>> if bcrypt.checkpw(password, hashed):
        ...     print("It Matches!")
        ... else:
        ...     print("It Does not Match :(")

    Maximum Password Length:
        The bcrypt algorithm only handles passwords up to 72 characters, any characters beyond that are ignored. To work around this, a common approach is to hash a password with a cryptographic hash (such as sha256) and then base64 encode it to prevent NULL byte problems before hashing the result with bcrypt:

        >>> password = b"an incredibly long password" * 10
        >>> hashed = bcrypt.hashpw(
        ...     base64.b64encode(hashlib.sha256(password).digest()),
        ...     bcrypt.gensalt()
        ... )       