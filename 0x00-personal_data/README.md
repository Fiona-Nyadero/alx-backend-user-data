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
