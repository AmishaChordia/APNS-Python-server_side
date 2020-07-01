import asyncio
from uuid import uuid4
from aioapns import APNs, NotificationRequest, PushType


async def send_push(token, title, subtitle, priority, additionalInfo):
    apns_key_client = APNs(
        key="My_APNS_Auth_Key.p8",
        key_id="FromApplePortal<p8 key id>",
        team_id="FromApplePortal<team id>",
        topic="com.your.bundleId",
        use_sandbox=True,
    )
    request = NotificationRequest(
        device_token=token,
        message={
            "aps": {
                "sound": "",
                "content-available": 1,
                "alert": {"title": title, "body": subtitle},
            },
            "anyAdditionalData": additionalInfo,
        },
        priority=priority,
        push_type=PushType.BACKGROUND if priority == "5" else PushType.ALERT,
    )

    await apns_key_client.send_notification(request)
    print("Fired notification on device {} with priority {}".format(token, priority))


loop = asyncio.get_event_loop()
loop.run_until_complete(
    send_push("APNS Device Token", "Title", "Subtitle Body", 10, "This is extra Info")
)

