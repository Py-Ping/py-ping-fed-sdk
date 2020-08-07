class EmailVerificationConfig():
    """A local identity email verification configuration.

    Attributes
    ----------
    emailVerificationEnabled : boolean
        Whether the email ownership verification is enabled.    emailVerificationErrorTemplateName : string
        The template name for email verification error.  The default is local.identity.email.verification.error.html.    emailVerificationSentTemplateName : string
        The template name for email verification sent. The default is local.identity.email.verification.sent.html.    emailVerificationSuccessTemplateName : string
        The template name for email verification success. The default is local.identity.email.verification.success.html.    fieldForEmailToVerify : string
        Field used for email ownership verification.<br>Note: Not required when emailVerificationEnabled is set to false.    fieldStoringVerificationStatus : string
        Field used for storing email verification status.<br>Note: Not required when emailVerificationEnabled is set to false.    notificationPublisherRef : str
        Reference to the associated notification publisher.    otlTimeToLive : integer
        Field used OTL time to live.  The default is 1440.    verifyEmailTemplateName : string
        The template name for verify email. The default is message-template-email-ownership-verification.html.
    """

    __slots__ = ["emailVerificationEnabled", "emailVerificationErrorTemplateName", "emailVerificationSentTemplateName", "emailVerificationSuccessTemplateName", "fieldForEmailToVerify", "fieldStoringVerificationStatus", "notificationPublisherRef", "otlTimeToLive", "verifyEmailTemplateName"]

    def __init__(self, fieldForEmailToVerify, fieldStoringVerificationStatus, emailVerificationEnabled=None, emailVerificationErrorTemplateName=None, emailVerificationSentTemplateName=None, emailVerificationSuccessTemplateName=None, notificationPublisherRef=None, otlTimeToLive=None, verifyEmailTemplateName=None):
        self.emailVerificationEnabled: bool = emailVerificationEnabled
        self.emailVerificationErrorTemplateName: str = emailVerificationErrorTemplateName
        self.emailVerificationSentTemplateName: str = emailVerificationSentTemplateName
        self.emailVerificationSuccessTemplateName: str = emailVerificationSuccessTemplateName
        self.fieldForEmailToVerify: str = fieldForEmailToVerify
        self.fieldStoringVerificationStatus: str = fieldStoringVerificationStatus
        self.notificationPublisherRef: str = notificationPublisherRef
        self.otlTimeToLive: str = otlTimeToLive
        self.verifyEmailTemplateName: str = verifyEmailTemplateName

    def _validate(self):
        return any(x for x in ['fieldForEmailToVerify', 'fieldStoringVerificationStatus'] if self.__dict__[x] is not None)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.__dict__})"

    def __str__(self):
        return f"{self.__dict__}"

    def __eq__(self, other):
        if isinstance(other, EmailVerificationConfig):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash((self.emailVerificationEnabled, self.emailVerificationErrorTemplateName, self.emailVerificationSentTemplateName, self.emailVerificationSuccessTemplateName, self.fieldForEmailToVerify, self.fieldStoringVerificationStatus, self.notificationPublisherRef, self.otlTimeToLive, self.verifyEmailTemplateName))

    @classmethod
    def from_dict(cls, python_dict):
        valid_data = {k: v for k, v in python_dict.items() if k in ["emailVerificationEnabled", "emailVerificationErrorTemplateName", "emailVerificationSentTemplateName", "emailVerificationSuccessTemplateName", "fieldForEmailToVerify", "fieldStoringVerificationStatus", "notificationPublisherRef", "otlTimeToLive", "verifyEmailTemplateName"]}

        return cls(**valid_data)

    def to_dict(self):
        return self.__dict__