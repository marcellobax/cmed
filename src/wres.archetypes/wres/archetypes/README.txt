Introduction
============

This is a full-blown functional test. The emphasis here is on testing what
the user may input and see, and the system is largely tested as a black box.
We use PloneTestCase to set up this test as well, so we have a full Plone site
to play with. We *can* inspect the state of the portal, e.g. using 
self.portal and self.folder, but it is often frowned upon since you are not
treating the system as a black box. Also, if you, for example, log in or set
roles using calls like self.setRoles(), these are not reflected in the test
browser, which runs as a separate session.

Being a doctest, we can tell a story here.

First, we must perform some setup. We use the testbrowser that is shipped
with Five, as this provides proper Zope 2 integration. Most of the 
documentation, though, is in the underlying zope.testbrower package.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

The following is useful when writing and debugging testbrowser tests. It lets
us see all error messages in the error_log.

    >>> self.portal.error_log._ignored_exceptions = ()

With that in place, we can go to the portal front page and log in. We will
do this using the default user from PloneTestCase:

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

Because add-on themes or products may remove or hide the login portlet, this test will use the login form that comes with plone.  

    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

Here, we set the value of the fields on the login form and then simulate a
submit click.  We then ensure that we get the friendly logged-in message:

    >>> "You are now logged in" in browser.contents
    True

Finally, let's return to the front page of our site before continuing

    >>> browser.open(portal_url)

-*- extra stuff goes here -*-
The CmedConfiguration content type
===============================

In this section we are tesing the CmedConfiguration content type by performing
basic operations like adding, updadating and deleting CmedConfiguration content
items.

Adding a new CmedConfiguration content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'CmedConfiguration' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CmedConfiguration').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CmedConfiguration' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CmedConfiguration Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'CmedConfiguration' content item to the portal.

Updating an existing CmedConfiguration content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New CmedConfiguration Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New CmedConfiguration Sample' in browser.contents
    True

Removing a/an CmedConfiguration content item
--------------------------------

If we go to the home page, we can see a tab with the 'New CmedConfiguration
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New CmedConfiguration Sample' in browser.contents
    True

Now we are going to delete the 'New CmedConfiguration Sample' object. First we
go to the contents tab and select the 'New CmedConfiguration Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New CmedConfiguration Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New CmedConfiguration
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New CmedConfiguration Sample' in browser.contents
    False

Adding a new CmedConfiguration content item as contributor
------------------------------------------------

Not only site managers are allowed to add CmedConfiguration content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'CmedConfiguration' and click the 'Add' button to get to the add form.

    >>> browser.getControl('CmedConfiguration').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'CmedConfiguration' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'CmedConfiguration Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new CmedConfiguration content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Visit content type
===============================

In this section we are tesing the Visit content type by performing
basic operations like adding, updadating and deleting Visit content
items.

Adding a new Visit content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Visit' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Visit').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Visit' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Visit Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Visit' content item to the portal.

Updating an existing Visit content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Visit Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Visit Sample' in browser.contents
    True

Removing a/an Visit content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Visit
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Visit Sample' in browser.contents
    True

Now we are going to delete the 'New Visit Sample' object. First we
go to the contents tab and select the 'New Visit Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Visit Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Visit
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Visit Sample' in browser.contents
    False

Adding a new Visit content item as contributor
------------------------------------------------

Not only site managers are allowed to add Visit content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Visit' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Visit').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Visit' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Visit Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Visit content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Impresso content type
===============================

In this section we are tesing the Impresso content type by performing
basic operations like adding, updadating and deleting Impresso content
items.

Adding a new Impresso content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Impresso' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Impresso').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Impresso' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Impresso Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Impresso' content item to the portal.

Updating an existing Impresso content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Impresso Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Impresso Sample' in browser.contents
    True

Removing a/an Impresso content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Impresso
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Impresso Sample' in browser.contents
    True

Now we are going to delete the 'New Impresso Sample' object. First we
go to the contents tab and select the 'New Impresso Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Impresso Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Impresso
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Impresso Sample' in browser.contents
    False

Adding a new Impresso content item as contributor
------------------------------------------------

Not only site managers are allowed to add Impresso content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Impresso' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Impresso').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Impresso' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Impresso Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Impresso content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Template content type
===============================

In this section we are tesing the Template content type by performing
basic operations like adding, updadating and deleting Template content
items.

Adding a new Template content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Template' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Template').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Template' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Template Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Template' content item to the portal.

Updating an existing Template content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Template Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Template Sample' in browser.contents
    True

Removing a/an Template content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Template
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Template Sample' in browser.contents
    True

Now we are going to delete the 'New Template Sample' object. First we
go to the contents tab and select the 'New Template Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Template Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Template
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Template Sample' in browser.contents
    False

Adding a new Template content item as contributor
------------------------------------------------

Not only site managers are allowed to add Template content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Template' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Template').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Template' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Template Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Template content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The TemplateFolder content type
===============================

In this section we are tesing the TemplateFolder content type by performing
basic operations like adding, updadating and deleting TemplateFolder content
items.

Adding a new TemplateFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'TemplateFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('TemplateFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'TemplateFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'TemplateFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'TemplateFolder' content item to the portal.

Updating an existing TemplateFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New TemplateFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New TemplateFolder Sample' in browser.contents
    True

Removing a/an TemplateFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New TemplateFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New TemplateFolder Sample' in browser.contents
    True

Now we are going to delete the 'New TemplateFolder Sample' object. First we
go to the contents tab and select the 'New TemplateFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New TemplateFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New TemplateFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New TemplateFolder Sample' in browser.contents
    False

Adding a new TemplateFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add TemplateFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'TemplateFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('TemplateFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'TemplateFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'TemplateFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new TemplateFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The GenericDocument content type
===============================

In this section we are tesing the GenericDocument content type by performing
basic operations like adding, updadating and deleting GenericDocument content
items.

Adding a new GenericDocument content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'GenericDocument' and click the 'Add' button to get to the add form.

    >>> browser.getControl('GenericDocument').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'GenericDocument' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'GenericDocument Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'GenericDocument' content item to the portal.

Updating an existing GenericDocument content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New GenericDocument Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New GenericDocument Sample' in browser.contents
    True

Removing a/an GenericDocument content item
--------------------------------

If we go to the home page, we can see a tab with the 'New GenericDocument
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New GenericDocument Sample' in browser.contents
    True

Now we are going to delete the 'New GenericDocument Sample' object. First we
go to the contents tab and select the 'New GenericDocument Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New GenericDocument Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New GenericDocument
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New GenericDocument Sample' in browser.contents
    False

Adding a new GenericDocument content item as contributor
------------------------------------------------

Not only site managers are allowed to add GenericDocument content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'GenericDocument' and click the 'Add' button to get to the add form.

    >>> browser.getControl('GenericDocument').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'GenericDocument' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'GenericDocument Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new GenericDocument content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The MedicalDocument content type
===============================

In this section we are tesing the MedicalDocument content type by performing
basic operations like adding, updadating and deleting MedicalDocument content
items.

Adding a new MedicalDocument content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'MedicalDocument' and click the 'Add' button to get to the add form.

    >>> browser.getControl('MedicalDocument').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'MedicalDocument' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'MedicalDocument Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'MedicalDocument' content item to the portal.

Updating an existing MedicalDocument content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New MedicalDocument Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New MedicalDocument Sample' in browser.contents
    True

Removing a/an MedicalDocument content item
--------------------------------

If we go to the home page, we can see a tab with the 'New MedicalDocument
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New MedicalDocument Sample' in browser.contents
    True

Now we are going to delete the 'New MedicalDocument Sample' object. First we
go to the contents tab and select the 'New MedicalDocument Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New MedicalDocument Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New MedicalDocument
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New MedicalDocument Sample' in browser.contents
    False

Adding a new MedicalDocument content item as contributor
------------------------------------------------

Not only site managers are allowed to add MedicalDocument content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'MedicalDocument' and click the 'Add' button to get to the add form.

    >>> browser.getControl('MedicalDocument').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'MedicalDocument' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'MedicalDocument Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new MedicalDocument content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The UploadChartFolder content type
===============================

In this section we are tesing the UploadChartFolder content type by performing
basic operations like adding, updadating and deleting UploadChartFolder content
items.

Adding a new UploadChartFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'UploadChartFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('UploadChartFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'UploadChartFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'UploadChartFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'UploadChartFolder' content item to the portal.

Updating an existing UploadChartFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New UploadChartFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New UploadChartFolder Sample' in browser.contents
    True

Removing a/an UploadChartFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New UploadChartFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New UploadChartFolder Sample' in browser.contents
    True

Now we are going to delete the 'New UploadChartFolder Sample' object. First we
go to the contents tab and select the 'New UploadChartFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New UploadChartFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New UploadChartFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New UploadChartFolder Sample' in browser.contents
    False

Adding a new UploadChartFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add UploadChartFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'UploadChartFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('UploadChartFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'UploadChartFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'UploadChartFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new UploadChartFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The ReviewOfSystems content type
===============================

In this section we are tesing the ReviewOfSystems content type by performing
basic operations like adding, updadating and deleting ReviewOfSystems content
items.

Adding a new ReviewOfSystems content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'ReviewOfSystems' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ReviewOfSystems').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ReviewOfSystems' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ReviewOfSystems Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'ReviewOfSystems' content item to the portal.

Updating an existing ReviewOfSystems content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New ReviewOfSystems Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New ReviewOfSystems Sample' in browser.contents
    True

Removing a/an ReviewOfSystems content item
--------------------------------

If we go to the home page, we can see a tab with the 'New ReviewOfSystems
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New ReviewOfSystems Sample' in browser.contents
    True

Now we are going to delete the 'New ReviewOfSystems Sample' object. First we
go to the contents tab and select the 'New ReviewOfSystems Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New ReviewOfSystems Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New ReviewOfSystems
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New ReviewOfSystems Sample' in browser.contents
    False

Adding a new ReviewOfSystems content item as contributor
------------------------------------------------

Not only site managers are allowed to add ReviewOfSystems content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'ReviewOfSystems' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ReviewOfSystems').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ReviewOfSystems' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ReviewOfSystems Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new ReviewOfSystems content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Clinic content type
===============================

In this section we are tesing the Clinic content type by performing
basic operations like adding, updadating and deleting Clinic content
items.

Adding a new Clinic content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Clinic' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Clinic').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Clinic' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Clinic Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Clinic' content item to the portal.

Updating an existing Clinic content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Clinic Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Clinic Sample' in browser.contents
    True

Removing a/an Clinic content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Clinic
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Clinic Sample' in browser.contents
    True

Now we are going to delete the 'New Clinic Sample' object. First we
go to the contents tab and select the 'New Clinic Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Clinic Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Clinic
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Clinic Sample' in browser.contents
    False

Adding a new Clinic content item as contributor
------------------------------------------------

Not only site managers are allowed to add Clinic content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Clinic' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Clinic').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Clinic' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Clinic Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Clinic content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Encounter content type
===============================

In this section we are tesing the Encounter content type by performing
basic operations like adding, updadating and deleting Encounter content
items.

Adding a new Encounter content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Encounter' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Encounter').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Encounter' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Encounter Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Encounter' content item to the portal.

Updating an existing Encounter content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Encounter Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Encounter Sample' in browser.contents
    True

Removing a/an Encounter content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Encounter
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Encounter Sample' in browser.contents
    True

Now we are going to delete the 'New Encounter Sample' object. First we
go to the contents tab and select the 'New Encounter Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Encounter Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Encounter
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Encounter Sample' in browser.contents
    False

Adding a new Encounter content item as contributor
------------------------------------------------

Not only site managers are allowed to add Encounter content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Encounter' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Encounter').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Encounter' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Encounter Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Encounter content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The VisitTemp content type
===============================

In this section we are tesing the VisitTemp content type by performing
basic operations like adding, updadating and deleting VisitTemp content
items.

Adding a new VisitTemp content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'VisitTemp' and click the 'Add' button to get to the add form.

    >>> browser.getControl('VisitTemp').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'VisitTemp' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'VisitTemp Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'VisitTemp' content item to the portal.

Updating an existing VisitTemp content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New VisitTemp Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New VisitTemp Sample' in browser.contents
    True

Removing a/an VisitTemp content item
--------------------------------

If we go to the home page, we can see a tab with the 'New VisitTemp
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New VisitTemp Sample' in browser.contents
    True

Now we are going to delete the 'New VisitTemp Sample' object. First we
go to the contents tab and select the 'New VisitTemp Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New VisitTemp Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New VisitTemp
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New VisitTemp Sample' in browser.contents
    False

Adding a new VisitTemp content item as contributor
------------------------------------------------

Not only site managers are allowed to add VisitTemp content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'VisitTemp' and click the 'Add' button to get to the add form.

    >>> browser.getControl('VisitTemp').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'VisitTemp' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'VisitTemp Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new VisitTemp content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Visit content type
===============================

In this section we are tesing the Visit content type by performing
basic operations like adding, updadating and deleting Visit content
items.

Adding a new Visit content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Visit' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Visit').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Visit' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Visit Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Visit' content item to the portal.

Updating an existing Visit content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Visit Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Visit Sample' in browser.contents
    True

Removing a/an Visit content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Visit
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Visit Sample' in browser.contents
    True

Now we are going to delete the 'New Visit Sample' object. First we
go to the contents tab and select the 'New Visit Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Visit Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Visit
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Visit Sample' in browser.contents
    False

Adding a new Visit content item as contributor
------------------------------------------------

Not only site managers are allowed to add Visit content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Visit' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Visit').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Visit' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Visit Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Visit content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The InsuranceFolder content type
===============================

In this section we are tesing the InsuranceFolder content type by performing
basic operations like adding, updadating and deleting InsuranceFolder content
items.

Adding a new InsuranceFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'InsuranceFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('InsuranceFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'InsuranceFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'InsuranceFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'InsuranceFolder' content item to the portal.

Updating an existing InsuranceFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New InsuranceFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New InsuranceFolder Sample' in browser.contents
    True

Removing a/an InsuranceFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New InsuranceFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New InsuranceFolder Sample' in browser.contents
    True

Now we are going to delete the 'New InsuranceFolder Sample' object. First we
go to the contents tab and select the 'New InsuranceFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New InsuranceFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New InsuranceFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New InsuranceFolder Sample' in browser.contents
    False

Adding a new InsuranceFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add InsuranceFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'InsuranceFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('InsuranceFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'InsuranceFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'InsuranceFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new InsuranceFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Insurance content type
===============================

In this section we are tesing the Insurance content type by performing
basic operations like adding, updadating and deleting Insurance content
items.

Adding a new Insurance content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Insurance' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Insurance').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Insurance' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Insurance Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Insurance' content item to the portal.

Updating an existing Insurance content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Insurance Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Insurance Sample' in browser.contents
    True

Removing a/an Insurance content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Insurance
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Insurance Sample' in browser.contents
    True

Now we are going to delete the 'New Insurance Sample' object. First we
go to the contents tab and select the 'New Insurance Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Insurance Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Insurance
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Insurance Sample' in browser.contents
    False

Adding a new Insurance content item as contributor
------------------------------------------------

Not only site managers are allowed to add Insurance content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Insurance' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Insurance').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Insurance' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Insurance Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Insurance content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The InitialVisit content type
===============================

In this section we are tesing the InitialVisit content type by performing
basic operations like adding, updadating and deleting InitialVisit content
items.

Adding a new InitialVisit content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'InitialVisit' and click the 'Add' button to get to the add form.

    >>> browser.getControl('InitialVisit').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'InitialVisit' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'InitialVisit Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'InitialVisit' content item to the portal.

Updating an existing InitialVisit content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New InitialVisit Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New InitialVisit Sample' in browser.contents
    True

Removing a/an InitialVisit content item
--------------------------------

If we go to the home page, we can see a tab with the 'New InitialVisit
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New InitialVisit Sample' in browser.contents
    True

Now we are going to delete the 'New InitialVisit Sample' object. First we
go to the contents tab and select the 'New InitialVisit Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New InitialVisit Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New InitialVisit
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New InitialVisit Sample' in browser.contents
    False

Adding a new InitialVisit content item as contributor
------------------------------------------------

Not only site managers are allowed to add InitialVisit content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'InitialVisit' and click the 'Add' button to get to the add form.

    >>> browser.getControl('InitialVisit').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'InitialVisit' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'InitialVisit Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new InitialVisit content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

The Visit content type
===============================

In this section we are tesing the Visit content type by performing
basic operations like adding, updadating and deleting Visit content
items.

Adding a new Visit content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Visit' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Visit').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Visit' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Visit Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Visit' content item to the portal.

Updating an existing Visit content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Visit Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Visit Sample' in browser.contents
    True

Removing a/an Visit content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Visit
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Visit Sample' in browser.contents
    True

Now we are going to delete the 'New Visit Sample' object. First we
go to the contents tab and select the 'New Visit Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Visit Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Visit
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Visit Sample' in browser.contents
    False

Adding a new Visit content item as contributor
------------------------------------------------

Not only site managers are allowed to add Visit content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Visit' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Visit').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Visit' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Visit Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Visit content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The VisitFolder content type
===============================

In this section we are tesing the VisitFolder content type by performing
basic operations like adding, updadating and deleting VisitFolder content
items.

Adding a new VisitFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'VisitFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('VisitFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'VisitFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'VisitFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'VisitFolder' content item to the portal.

Updating an existing VisitFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New VisitFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New VisitFolder Sample' in browser.contents
    True

Removing a/an VisitFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New VisitFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New VisitFolder Sample' in browser.contents
    True

Now we are going to delete the 'New VisitFolder Sample' object. First we
go to the contents tab and select the 'New VisitFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New VisitFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New VisitFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New VisitFolder Sample' in browser.contents
    False

Adding a new VisitFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add VisitFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'VisitFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('VisitFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'VisitFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'VisitFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new VisitFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The ProgressNotes content type
===============================

In this section we are tesing the ProgressNotes content type by performing
basic operations like adding, updadating and deleting ProgressNotes content
items.

Adding a new ProgressNotes content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'ProgressNotes' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ProgressNotes').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ProgressNotes' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ProgressNotes Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'ProgressNotes' content item to the portal.

Updating an existing ProgressNotes content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New ProgressNotes Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New ProgressNotes Sample' in browser.contents
    True

Removing a/an ProgressNotes content item
--------------------------------

If we go to the home page, we can see a tab with the 'New ProgressNotes
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New ProgressNotes Sample' in browser.contents
    True

Now we are going to delete the 'New ProgressNotes Sample' object. First we
go to the contents tab and select the 'New ProgressNotes Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New ProgressNotes Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New ProgressNotes
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New ProgressNotes Sample' in browser.contents
    False

Adding a new ProgressNotes content item as contributor
------------------------------------------------

Not only site managers are allowed to add ProgressNotes content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'ProgressNotes' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ProgressNotes').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ProgressNotes' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ProgressNotes Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new ProgressNotes content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The ReferringProviderFolder content type
===============================

In this section we are tesing the ReferringProviderFolder content type by performing
basic operations like adding, updadating and deleting ReferringProviderFolder content
items.

Adding a new ReferringProviderFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'ReferringProviderFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ReferringProviderFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ReferringProviderFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ReferringProviderFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'ReferringProviderFolder' content item to the portal.

Updating an existing ReferringProviderFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New ReferringProviderFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New ReferringProviderFolder Sample' in browser.contents
    True

Removing a/an ReferringProviderFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New ReferringProviderFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New ReferringProviderFolder Sample' in browser.contents
    True

Now we are going to delete the 'New ReferringProviderFolder Sample' object. First we
go to the contents tab and select the 'New ReferringProviderFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New ReferringProviderFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New ReferringProviderFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New ReferringProviderFolder Sample' in browser.contents
    False

Adding a new ReferringProviderFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add ReferringProviderFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'ReferringProviderFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ReferringProviderFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ReferringProviderFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ReferringProviderFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new ReferringProviderFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The ReferringProvider content type
===============================

In this section we are tesing the ReferringProvider content type by performing
basic operations like adding, updadating and deleting ReferringProvider content
items.

Adding a new ReferringProvider content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'ReferringProvider' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ReferringProvider').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ReferringProvider' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ReferringProvider Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'ReferringProvider' content item to the portal.

Updating an existing ReferringProvider content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New ReferringProvider Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New ReferringProvider Sample' in browser.contents
    True

Removing a/an ReferringProvider content item
--------------------------------

If we go to the home page, we can see a tab with the 'New ReferringProvider
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New ReferringProvider Sample' in browser.contents
    True

Now we are going to delete the 'New ReferringProvider Sample' object. First we
go to the contents tab and select the 'New ReferringProvider Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New ReferringProvider Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New ReferringProvider
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New ReferringProvider Sample' in browser.contents
    False

Adding a new ReferringProvider content item as contributor
------------------------------------------------

Not only site managers are allowed to add ReferringProvider content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'ReferringProvider' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ReferringProvider').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ReferringProvider' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ReferringProvider Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new ReferringProvider content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The AdminFolder content type
===============================

In this section we are tesing the AdminFolder content type by performing
basic operations like adding, updadating and deleting AdminFolder content
items.

Adding a new AdminFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'AdminFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AdminFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AdminFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AdminFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'AdminFolder' content item to the portal.

Updating an existing AdminFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New AdminFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New AdminFolder Sample' in browser.contents
    True

Removing a/an AdminFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New AdminFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New AdminFolder Sample' in browser.contents
    True

Now we are going to delete the 'New AdminFolder Sample' object. First we
go to the contents tab and select the 'New AdminFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New AdminFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New AdminFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New AdminFolder Sample' in browser.contents
    False

Adding a new AdminFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add AdminFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'AdminFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('AdminFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'AdminFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'AdminFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new AdminFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Admin content type
===============================

In this section we are tesing the Admin content type by performing
basic operations like adding, updadating and deleting Admin content
items.

Adding a new Admin content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Admin' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Admin').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Admin' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Admin Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Admin' content item to the portal.

Updating an existing Admin content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Admin Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Admin Sample' in browser.contents
    True

Removing a/an Admin content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Admin
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Admin Sample' in browser.contents
    True

Now we are going to delete the 'New Admin Sample' object. First we
go to the contents tab and select the 'New Admin Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Admin Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Admin
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Admin Sample' in browser.contents
    False

Adding a new Admin content item as contributor
------------------------------------------------

Not only site managers are allowed to add Admin content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Admin' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Admin').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Admin' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Admin Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Admin content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The DocPlastica content type
===============================

In this section we are tesing the DocPlastica content type by performing
basic operations like adding, updadating and deleting DocPlastica content
items.

Adding a new DocPlastica content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'DocPlastica' and click the 'Add' button to get to the add form.

    >>> browser.getControl('DocPlastica').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'DocPlastica' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'DocPlastica Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'DocPlastica' content item to the portal.

Updating an existing DocPlastica content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New DocPlastica Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New DocPlastica Sample' in browser.contents
    True

Removing a/an DocPlastica content item
--------------------------------

If we go to the home page, we can see a tab with the 'New DocPlastica
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New DocPlastica Sample' in browser.contents
    True

Now we are going to delete the 'New DocPlastica Sample' object. First we
go to the contents tab and select the 'New DocPlastica Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New DocPlastica Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New DocPlastica
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New DocPlastica Sample' in browser.contents
    False

Adding a new DocPlastica content item as contributor
------------------------------------------------

Not only site managers are allowed to add DocPlastica content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'DocPlastica' and click the 'Add' button to get to the add form.

    >>> browser.getControl('DocPlastica').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'DocPlastica' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'DocPlastica Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new DocPlastica content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The DocBoletim content type
===============================

In this section we are tesing the DocBoletim content type by performing
basic operations like adding, updadating and deleting DocBoletim content
items.

Adding a new DocBoletim content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'DocBoletim' and click the 'Add' button to get to the add form.

    >>> browser.getControl('DocBoletim').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'DocBoletim' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'DocBoletim Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'DocBoletim' content item to the portal.

Updating an existing DocBoletim content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New DocBoletim Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New DocBoletim Sample' in browser.contents
    True

Removing a/an DocBoletim content item
--------------------------------

If we go to the home page, we can see a tab with the 'New DocBoletim
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New DocBoletim Sample' in browser.contents
    True

Now we are going to delete the 'New DocBoletim Sample' object. First we
go to the contents tab and select the 'New DocBoletim Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New DocBoletim Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New DocBoletim
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New DocBoletim Sample' in browser.contents
    False

Adding a new DocBoletim content item as contributor
------------------------------------------------

Not only site managers are allowed to add DocBoletim content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'DocBoletim' and click the 'Add' button to get to the add form.

    >>> browser.getControl('DocBoletim').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'DocBoletim' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'DocBoletim Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new DocBoletim content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The ExamFolder content type
===============================

In this section we are tesing the ExamFolder content type by performing
basic operations like adding, updadating and deleting ExamFolder content
items.

Adding a new ExamFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'ExamFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ExamFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ExamFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ExamFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'ExamFolder' content item to the portal.

Updating an existing ExamFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New ExamFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New ExamFolder Sample' in browser.contents
    True

Removing a/an ExamFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New ExamFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New ExamFolder Sample' in browser.contents
    True

Now we are going to delete the 'New ExamFolder Sample' object. First we
go to the contents tab and select the 'New ExamFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New ExamFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New ExamFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New ExamFolder Sample' in browser.contents
    False

Adding a new ExamFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add ExamFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'ExamFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ExamFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ExamFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ExamFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new ExamFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The DocumentFolder content type
===============================

In this section we are tesing the DocumentFolder content type by performing
basic operations like adding, updadating and deleting DocumentFolder content
items.

Adding a new DocumentFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'DocumentFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('DocumentFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'DocumentFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'DocumentFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'DocumentFolder' content item to the portal.

Updating an existing DocumentFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New DocumentFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New DocumentFolder Sample' in browser.contents
    True

Removing a/an DocumentFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New DocumentFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New DocumentFolder Sample' in browser.contents
    True

Now we are going to delete the 'New DocumentFolder Sample' object. First we
go to the contents tab and select the 'New DocumentFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New DocumentFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New DocumentFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New DocumentFolder Sample' in browser.contents
    False

Adding a new DocumentFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add DocumentFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'DocumentFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('DocumentFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'DocumentFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'DocumentFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new DocumentFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The ChartFolder content type
===============================

In this section we are tesing the ChartFolder content type by performing
basic operations like adding, updadating and deleting ChartFolder content
items.

Adding a new ChartFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'ChartFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ChartFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ChartFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ChartFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'ChartFolder' content item to the portal.

Updating an existing ChartFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New ChartFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New ChartFolder Sample' in browser.contents
    True

Removing a/an ChartFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New ChartFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New ChartFolder Sample' in browser.contents
    True

Now we are going to delete the 'New ChartFolder Sample' object. First we
go to the contents tab and select the 'New ChartFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New ChartFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New ChartFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New ChartFolder Sample' in browser.contents
    False

Adding a new ChartFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add ChartFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'ChartFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('ChartFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'ChartFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'ChartFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new ChartFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The WRESUser content type
===============================

In this section we are tesing the WRESUser content type by performing
basic operations like adding, updadating and deleting WRESUser content
items.

Adding a new WRESUser content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'WRESUser' and click the 'Add' button to get to the add form.

    >>> browser.getControl('WRESUser').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'WRESUser' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'WRESUser Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'WRESUser' content item to the portal.

Updating an existing WRESUser content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New WRESUser Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New WRESUser Sample' in browser.contents
    True

Removing a/an WRESUser content item
--------------------------------

If we go to the home page, we can see a tab with the 'New WRESUser
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New WRESUser Sample' in browser.contents
    True

Now we are going to delete the 'New WRESUser Sample' object. First we
go to the contents tab and select the 'New WRESUser Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New WRESUser Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New WRESUser
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New WRESUser Sample' in browser.contents
    False

Adding a new WRESUser content item as contributor
------------------------------------------------

Not only site managers are allowed to add WRESUser content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'WRESUser' and click the 'Add' button to get to the add form.

    >>> browser.getControl('WRESUser').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'WRESUser' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'WRESUser Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new WRESUser content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The TranscriptionistFolder content type
===============================

In this section we are tesing the TranscriptionistFolder content type by performing
basic operations like adding, updadating and deleting TranscriptionistFolder content
items.

Adding a new TranscriptionistFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'TranscriptionistFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('TranscriptionistFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'TranscriptionistFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'TranscriptionistFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'TranscriptionistFolder' content item to the portal.

Updating an existing TranscriptionistFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New TranscriptionistFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New TranscriptionistFolder Sample' in browser.contents
    True

Removing a/an TranscriptionistFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New TranscriptionistFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New TranscriptionistFolder Sample' in browser.contents
    True

Now we are going to delete the 'New TranscriptionistFolder Sample' object. First we
go to the contents tab and select the 'New TranscriptionistFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New TranscriptionistFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New TranscriptionistFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New TranscriptionistFolder Sample' in browser.contents
    False

Adding a new TranscriptionistFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add TranscriptionistFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'TranscriptionistFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('TranscriptionistFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'TranscriptionistFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'TranscriptionistFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new TranscriptionistFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Transcriptionist content type
===============================

In this section we are tesing the Transcriptionist content type by performing
basic operations like adding, updadating and deleting Transcriptionist content
items.

Adding a new Transcriptionist content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Transcriptionist' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Transcriptionist').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Transcriptionist' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Transcriptionist Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Transcriptionist' content item to the portal.

Updating an existing Transcriptionist content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Transcriptionist Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Transcriptionist Sample' in browser.contents
    True

Removing a/an Transcriptionist content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Transcriptionist
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Transcriptionist Sample' in browser.contents
    True

Now we are going to delete the 'New Transcriptionist Sample' object. First we
go to the contents tab and select the 'New Transcriptionist Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Transcriptionist Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Transcriptionist
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Transcriptionist Sample' in browser.contents
    False

Adding a new Transcriptionist content item as contributor
------------------------------------------------

Not only site managers are allowed to add Transcriptionist content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Transcriptionist' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Transcriptionist').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Transcriptionist' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Transcriptionist Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Transcriptionist content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The SecretaryFolder content type
===============================

In this section we are tesing the SecretaryFolder content type by performing
basic operations like adding, updadating and deleting SecretaryFolder content
items.

Adding a new SecretaryFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'SecretaryFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('SecretaryFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'SecretaryFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'SecretaryFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'SecretaryFolder' content item to the portal.

Updating an existing SecretaryFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New SecretaryFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New SecretaryFolder Sample' in browser.contents
    True

Removing a/an SecretaryFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New SecretaryFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New SecretaryFolder Sample' in browser.contents
    True

Now we are going to delete the 'New SecretaryFolder Sample' object. First we
go to the contents tab and select the 'New SecretaryFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New SecretaryFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New SecretaryFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New SecretaryFolder Sample' in browser.contents
    False

Adding a new SecretaryFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add SecretaryFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'SecretaryFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('SecretaryFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'SecretaryFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'SecretaryFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new SecretaryFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Secretary content type
===============================

In this section we are tesing the Secretary content type by performing
basic operations like adding, updadating and deleting Secretary content
items.

Adding a new Secretary content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Secretary' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Secretary').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Secretary' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Secretary Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Secretary' content item to the portal.

Updating an existing Secretary content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Secretary Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Secretary Sample' in browser.contents
    True

Removing a/an Secretary content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Secretary
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Secretary Sample' in browser.contents
    True

Now we are going to delete the 'New Secretary Sample' object. First we
go to the contents tab and select the 'New Secretary Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Secretary Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Secretary
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Secretary Sample' in browser.contents
    False

Adding a new Secretary content item as contributor
------------------------------------------------

Not only site managers are allowed to add Secretary content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Secretary' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Secretary').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Secretary' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Secretary Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Secretary content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Patient content type
===============================

In this section we are tesing the Patient content type by performing
basic operations like adding, updadating and deleting Patient content
items.

Adding a new Patient content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Patient' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Patient').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Patient' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Patient Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Patient' content item to the portal.

Updating an existing Patient content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Patient Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Patient Sample' in browser.contents
    True

Removing a/an Patient content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Patient
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Patient Sample' in browser.contents
    True

Now we are going to delete the 'New Patient Sample' object. First we
go to the contents tab and select the 'New Patient Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Patient Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Patient
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Patient Sample' in browser.contents
    False

Adding a new Patient content item as contributor
------------------------------------------------

Not only site managers are allowed to add Patient content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Patient' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Patient').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Patient' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Patient Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Patient content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Doctor content type
===============================

In this section we are tesing the Doctor content type by performing
basic operations like adding, updadating and deleting Doctor content
items.

Adding a new Doctor content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Doctor' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Doctor').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Doctor' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Doctor Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Doctor' content item to the portal.

Updating an existing Doctor content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Doctor Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Doctor Sample' in browser.contents
    True

Removing a/an Doctor content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Doctor
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Doctor Sample' in browser.contents
    True

Now we are going to delete the 'New Doctor Sample' object. First we
go to the contents tab and select the 'New Doctor Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Doctor Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Doctor
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Doctor Sample' in browser.contents
    False

Adding a new Doctor content item as contributor
------------------------------------------------

Not only site managers are allowed to add Doctor content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Doctor' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Doctor').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Doctor' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Doctor Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Doctor content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The PatientFolder content type
===============================

In this section we are tesing the PatientFolder content type by performing
basic operations like adding, updadating and deleting PatientFolder content
items.

Adding a new PatientFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'PatientFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('PatientFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'PatientFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'PatientFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'PatientFolder' content item to the portal.

Updating an existing PatientFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New PatientFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New PatientFolder Sample' in browser.contents
    True

Removing a/an PatientFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New PatientFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New PatientFolder Sample' in browser.contents
    True

Now we are going to delete the 'New PatientFolder Sample' object. First we
go to the contents tab and select the 'New PatientFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New PatientFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New PatientFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New PatientFolder Sample' in browser.contents
    False

Adding a new PatientFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add PatientFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'PatientFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('PatientFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'PatientFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'PatientFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new PatientFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Patient content type
===============================

In this section we are tesing the Patient content type by performing
basic operations like adding, updadating and deleting Patient content
items.

Adding a new Patient content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Patient' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Patient').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Patient' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Patient Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Patient' content item to the portal.

Updating an existing Patient content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Patient Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Patient Sample' in browser.contents
    True

Removing a/an Patient content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Patient
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Patient Sample' in browser.contents
    True

Now we are going to delete the 'New Patient Sample' object. First we
go to the contents tab and select the 'New Patient Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Patient Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Patient
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Patient Sample' in browser.contents
    False

Adding a new Patient content item as contributor
------------------------------------------------

Not only site managers are allowed to add Patient content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Patient' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Patient').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Patient' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Patient Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Patient content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The DoctorFolder content type
===============================

In this section we are tesing the DoctorFolder content type by performing
basic operations like adding, updadating and deleting DoctorFolder content
items.

Adding a new DoctorFolder content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'DoctorFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('DoctorFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'DoctorFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'DoctorFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'DoctorFolder' content item to the portal.

Updating an existing DoctorFolder content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New DoctorFolder Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New DoctorFolder Sample' in browser.contents
    True

Removing a/an DoctorFolder content item
--------------------------------

If we go to the home page, we can see a tab with the 'New DoctorFolder
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New DoctorFolder Sample' in browser.contents
    True

Now we are going to delete the 'New DoctorFolder Sample' object. First we
go to the contents tab and select the 'New DoctorFolder Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New DoctorFolder Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New DoctorFolder
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New DoctorFolder Sample' in browser.contents
    False

Adding a new DoctorFolder content item as contributor
------------------------------------------------

Not only site managers are allowed to add DoctorFolder content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'DoctorFolder' and click the 'Add' button to get to the add form.

    >>> browser.getControl('DoctorFolder').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'DoctorFolder' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'DoctorFolder Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new DoctorFolder content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


The Doctor content type
===============================

In this section we are tesing the Doctor content type by performing
basic operations like adding, updadating and deleting Doctor content
items.

Adding a new Doctor content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Doctor' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Doctor').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Doctor' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Doctor Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Doctor' content item to the portal.

Updating an existing Doctor content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Doctor Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Doctor Sample' in browser.contents
    True

Removing a/an Doctor content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Doctor
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Doctor Sample' in browser.contents
    True

Now we are going to delete the 'New Doctor Sample' object. First we
go to the contents tab and select the 'New Doctor Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Doctor Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Doctor
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Doctor Sample' in browser.contents
    False

Adding a new Doctor content item as contributor
------------------------------------------------

Not only site managers are allowed to add Doctor content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Doctor' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Doctor').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Doctor' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Doctor Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Doctor content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)



