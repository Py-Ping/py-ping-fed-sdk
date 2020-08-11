class EmailVerificationConfig():
    """A local identity email verification configuration.

    Attributes
    ----------
    emailVerificationEnabled : boolean
        Whether the email ownership verification is enabled.
    emailVerificationErrorTemplateName : string
        The template name for email verification error.  The default is local.identity.email.verification.error.html.
    emailVerificationSentTemplateName : string
        The template name for email verification sent. The default is local.identity.email.verification.sent.html.
    emailVerificationSuccessTemplateName : string
        The template name for email verification success. The default is local.identity.email.verification.success.html.
    fieldForEmailToVerify : string
        Field used for email ownership verification.<br>Note: Not required when emailVerificationEnabled is set to false.
    fieldStoringVerificationStatus : string
        Field used for storing email verification status.<br>Note: Not required when emailVerificationEnabled is set to false.
    notificationPublisherRef : str
        Reference to the associated notification publisher.
    otlTimeToLive : integer
        Field used OTL time to live.  The default is 1440.
    verifyEmailTemplateName : string
        The template name for verify email. The default is message-template-email-ownership-verification.html.

    """

    def __init__(self, fieldForEmailToVerify:str, fieldStoringVerificationStatus:str, emailVerificationEnabled:bool=None, emailVerificationErrorTemplateName:str=None, emailVerificationSentTemplateName:str=None, emailVerificationSuccessTemplateName:str=None, notificationPublisherRef=None, otlTimeToLive:int=None, verifyEmailTemplateName:str=None) -> None:
        self.emailVerificationEnabled = emailVerificationEnabled
        self.emailVerificationErrorTemplateName = emailVerificationErrorTemplateName
        self.emailVerificationSentTemplateName = emailVerificationSentTemplateName
        self.emailVerificationSuccessTemplateName = emailVerificationSuccessTemplateName
        self.fieldForEmailToVerify = fieldForEmailToVerify
        self.fieldStoringVerificationStatus = fieldStoringVerificationStatus
        self.notificationPublisherRef = notificationPublisherRef
        self.otlTimeToLive = otlTimeToLive
        self.verifyEmailTemplateName = verifyEmailTemplateName

    def _validate(self) -> bool:
        return any(x for x in ["fieldForEmailToVerify", "fieldStoringVerificationStatus"] if self.__dict__[x] is not None)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self) -> str:
        return f"{self.__dict__}"

    def __eq__(self, other) -> bool:
        if isinstance(other, EmailVerificationConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self) -> int:
        return hash(frozenset(self.emailVerificationEnabled, self.emailVerificationErrorTemplateName, self.emailVerificationSentTemplateName, self.emailVerificationSuccessTemplateName, self.fieldForEmailToVerify, self.fieldStoringVerificationStatus, self.notificationPublisherRef, self.otlTimeToLive, self.verifyEmailTemplateName))

    @classmethod
    def from_dict(cls, python_dict: dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["emailVerificationEnabled", "emailVerificationErrorTemplateName", "emailVerificationSentTemplateName", "emailVerificationSuccessTemplateName", "fieldForEmailToVerify", "fieldStoringVerificationStatus", "notificationPublisherRef", "otlTimeToLive", "verifyEmailTemplateName"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__