import pandas as pd
import time
from pprint import pprint
from office365.sharepoint.client_context import ClientContext
from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext
from office365.sharepoint.files.file import File
from office365.sharepoint.folders.folder import Folder

# USER_NAME = "ctchow@DONGHWATelecom.onmicrosoft.com"
# PASSWORD = "Vam44078Vam44078"
USER_NAME = "DONGHWA17@DONGHWATelecom.onmicrosoft.com"
PASSWORD = "Vam1874Vam1874"


def main1():
    user_credentials = UserCredential(USER_NAME, PASSWORD)
    ctx = ClientContext(
        "https://donghwatelecom.sharepoint.com/sites/LeaveApplication"
    ).with_credentials(user_credentials)
    list_title = "LeaveDB"
    list_to_export = ctx.web.lists.get_by_title(list_title)
    pprint(list_to_export.context)
    list_items = list_to_export.items.get().execute_query()

    dict_list = []
    for item in list_items:
        dict_list.append(item.properties)

    df = pd.DataFrame.from_records(dict_list)
    df.to_excel("LeaveDB3.xlsx", index=False)


def main2():
    user_credentials = UserCredential(USER_NAME, PASSWORD)
    ctx = ClientContext(
        "https://donghwatelecom.sharepoint.com/sites/LeaveApplication"
    ).with_credentials(user_credentials)
    list_title = "LeaveForm"
    list_to_export = ctx.web.lists.get_by_title(list_title)
    list_items = list_to_export.items.get().execute_query()

    dict_list = []
    for item in list_items:
        dict_list.append(item.properties)

    df = pd.DataFrame.from_records(dict_list)
    df.to_excel("LeaveForm2.xlsx", index=False)


def main3():
    user_credentials = UserCredential(USER_NAME, PASSWORD)
    ctx = ClientContext(
        "https://donghwatelecom.sharepoint.com/sites/LeaveApplication"
    ).with_credentials(user_credentials)
    list_title = "LeaveForm"
    list_to_export = ctx.web.lists.get_by_title(list_title)
    print(list_to_export.context.base_url)
    list_items = list_to_export.items.get().execute_query()

    dict_list = []
    update_item_list = []
    for item in list_items:
        if item.properties["EmpName"] == "國分最帥":
            update_item_list.append(item)
            dict_list.append(item.properties)

    # df = pd.DataFrame.from_records(dict_list)
    # print(df)
    for item in update_item_list:
        item.set_property("EmpName", "處長2號").update().execute_query()
        print("Item has been updated")


def main4():
    user_credentials = UserCredential(USER_NAME, PASSWORD)
    ctx = ClientContext(
        "https://donghwatelecom.sharepoint.com/sites/LeaveApplication"
    ).with_credentials(user_credentials)
    list_title = "LeaveForm"
    list_to_export = ctx.web.lists.get_by_title(list_title)
    list_items = list_to_export.items.get().execute_query()

    for item in list_items:
        print(item.properties["Id"])
        if item.properties["Id"] == 475:
            print("Found")
            list_to_export.get_item_by_id(
                item.properties["Id"]
            ).delete_object().execute_query()
            print("Item has been deleted")


def download_attachment():
    user_credentials = UserCredential(USER_NAME, PASSWORD)
    ctx = ClientContext(
        "https://donghwatelecom.sharepoint.com/sites/LeaveApplication"
    ).with_credentials(user_credentials)

    list_title = "LeaveForm"
    source_list = ctx.web.lists.get_by_title(list_title)
    items = source_list.items
    for item_ in items:
        print("-" * 50)
        print(item_.properties["EmpName"])
        print("-" * 50)
    ctx.load(items, ["Attachments"])
    ctx.execute_query()
    for item in items:
        if item.properties["Attachments"]:
            print(item.properties["Attachments"])
            # 1. determine whether ListItem contains attachments
            # 2. Explicitly load attachments for ListItem
            attachment_files = item.attachment_files.get().execute_query()
            # 3. Enumerate and save attachments
            for attachment_file in attachment_files:
                download_file_name = f"./attachment/{attachment_file.file_name}"
                with open(download_file_name, "wb") as fh:
                    attachment_file.download(fh).execute_query()
                print(
                    f"{attachment_file.server_relative_url} has been downloaded into {download_file_name}"
                )


def read_attachment():
    user_credentials = UserCredential(USER_NAME, PASSWORD)
    ctx = ClientContext(
        "https://donghwatelecom.sharepoint.com/sites/LeaveApplication"
    ).with_credentials(user_credentials)

    list_title = "LeaveForm"
    source_list = ctx.web.lists.get_by_title(list_title)
    items = (
        source_list.items.select(["Attachments"])
        .expand(["AttachmentFiles"])
        .get()
        .execute_query()
    )
    for item in items:
        for attachment_file in item.attachment_files:
            download_file_name = f"./attachment/{attachment_file.file_name}"
            with open(download_file_name, "wb") as fh:
                attachment_file.download(fh).execute_query()
            print(f"{attachment_file.server_relative_url}")


if __name__ == "__main__":
    # LeaveForm URL: https://donghwatelecom.sharepoint.com/sites/LeaveApplication/Lists/LeaveForm/AllItems.aspx
    # LeaveDB URL: https://donghwatelecom.sharepoint.com/sites/LeaveApplication/Lists/LeaveDB/AllItems.aspx
    start_time = time.time()
    # main1()
    main2()
    # main3()
    # main4()
    # download_attachment()
    # read_attachment()
    print("--- %s seconds ---" % (time.time() - start_time))
