Release process of the ESL Bundle
=================================

Workflow
--------

The development of the ESL Bundle is managed using the `Gitlab
Flow <https://docs.gitlab.com/ee/workflow/gitlab_flow.html>`__. The
*master* branch is where all accepted changes are merged and is the only
permanent branch. In addition, release branches exist for the lifetime
of maintained releases, in order to deal with release-specific bugfixes.

All changes made to the ESL Bundle must first be submitted by `creating
an issue <https://gitlab.com/ElectronicStructureLibrary/esl-bundle/issues>`__
on the Gitlab repository of the bundle. Once accepted, one or more
branches are created to perform the tasks necessary to solve the issue.
Once the solution passes all *Continuous Integration (CI)* pipelines of
the ESL Bundle and has been peer-reviewed, it is merged to the appropriate
branch of the bundle. The CI and merging are done through a *Merge Request*
on Gitlab.

There are 2 main kinds of issues that affect the evolution of the ESL Bundle:

- bugfixes and feedback;
- proposals for changes.

Any kind of issue can be created at any time. Bugfixes are usually merged into
a *hotfix* branch for the current release of the bundle, while proposals for
changes are collected and examined at specific dates.


Bugfixes
--------

Bugfix issues are problems related to the current release of the bundle, under
the explicit restrictions that their solution must neither add nor remove
packages, plus the obligation of preserving their APIs. All other issues are
considered as *proposals for changes* and addressed differently.

Bugfixes are integrated in priority into the current release of the bundle,
except when in the final stages of publishing a new release. If they
correspond to a problem encountered in a component of the bundle, they are
usually solved through the provision of patches applied during the build of
the bundle. They rarely involve a version upgrade of this component. Bugfixes
related to the bundle itself may involve any kind of operation.


Proposals for changes
---------------------

Changes to the ESL Bundle can be proposed at any time. When opening an
issue for the bundle on Gitlab, a user or developer is notifying all the
stakeholders of the bundle about *proposed changes*. These changes can
be of 4 different types:

-  requesting the addition of a new package into the bundle;
-  requesting the upgrade of a package in the bundle;
-  requesting the removal of a package from the bundle.

In order to keep the scope of the discussions focused, one issue has to
be submitted for each individual package. The person submitting the
issue is also encouraged to use the *tags*\ and *milestone* fields of
the issue submission form to make their intentions clearer.

In order to simplify the processing of the issue, its title has to be as
relevant and concise as possible. For a better triage of the issues, it
is highly recommended to prefix the title with a keyword:

-  [bundle] for an addition to the bundle and for bugfixes affecting the
   whole bundle;
-  [package], where *package* is the name of the affected package, for
   all other kinds of issues.

The ESL Bundle also provides issue templates which should be used
whenever possible.

Bugfixes will be considered at all times. However, additions, upgrades,
and removals of packages will only be considered for the upcoming
release during specific periods of time (see below). Late submissions
will systematically be triaged to the following release(s).


Release cycle
-------------

A release cycle of the ESL Bundle starts with the creation of a
milestone for the upcoming version. The start date of the milestone
defines the start of the release process and its end date corresponds to
the publication of the new bundle version. Once the milestone is
available, it is populated with the Gitlab issues of the proposed
changes that had to be postponed during the previous release cycle.

The release cycle is divided into 3 stages:

-  the *bugfix stage*, to solve technical issues within the published
   bundle releases;
-  the *discussion stage*, starting at the same date as the latest
   milestone, to decide which of the changes proposed until then will be
   included in the upcoming bundle release;
-  the *integration stage*, to include all accepted changes into the
   bundle.

Once the release process is completed, the ESL curating team goes
through the remaining Gitlab issues and sets a version number for the
next release, which will be used to create the next milestone. All
changes marked as postponed for the current release cycle are
immediately added to the new milestone.


Release management
------------------

Active releases
~~~~~~~~~~~~~~~

There are at most 3 releases of the ESL Bundle maintained at a given
moment in time:

-  the *upcoming* one, which exists between the start and end dates of
   the corresponding milestone;
-  the *stable* one, which was published at the end of the previous
   release cycle;
-  the *old-stable* one, corresponding to the release version published
   one release cycle before the *stable* release.

At the end of a release cycle, the *upcoming* release is rolled out as
the new *stable* one, the former *stable* release is renamed
*old-stable*, and the former *old-stable* one is discarded.

In the *stable* release, the only accepted changes are bugfixes that do
not require any change for individual package versions. Changes to the
source code of individual ESL Bundle components will be applied through
patches and reported upstream whenever relevant. Fixes can be sent at
any time.

The *old-stable* release only accepts bugfixes marked as *critical*.
They can only be proposed during the *bugfix stage* of the release
cycle.

.. note:: Once published, a release is maintained for one year. If justified,
   an archive can be kept available for a longer time. However, after the
   one-year maintenance period, no changes will be accepted anymore.


Bugfix stage
~~~~~~~~~~~~

During the *bugfix stage*, any issue created on the Gitlab repository of
the bundle can be considered for the upcoming release and added to the
corresponding milestone. Please note that *considered* does not mean
*accepted*, and that the only merge requests allowed during this stage
are those which solve issues for already published ESL Bundle releases.


Discussion stage
~~~~~~~~~~~~~~~~

The *discussion stage* begins with collecting the proposed changes which
have been submitted before the start date of the current milestone. An
issue is created from this collection and a new version of the
``README`` file of the ESL Bundle with the new composition of the bundle
is provided in a corresponding branch. A merge request is then created
and all relevant stakeholders are notified through appropriate channels.
This marks the official beginning of the discussions.

THe *ESL Steering Committee* is in charge of reviewing the merge request
and debating the proposed changes. Each change proposal can end up in
one of 3 states:

-  accepted for the upcoming release, in which case further discussion
   will take place in the original issue of the change proposal;
-  rejected, if practical problems like severe icompatibilities prevent
   its implementation into the bundle;
-  postponed, if significant changes have to be made to the bundle
   and/or individual packages for the proposal to be implemented and
   such changes cannot be completed before the end date of the
   milestone.

Once all change proposals have been reviewed, the only changes that can
be accepted for the upcoming release are those coming from the feedback
of the *integration stage*.


Integration stage
~~~~~~~~~~~~~~~~~

The *integration stage* formally starts when all change proposals have
been reviewed during the *discussion stage*. However, individual
packages may begin with the integration efforts as soon as the
corresponding proposal has been accepted.

This particular stage requires a tight collaboration between the ESL
Curating Team and the developers of the individual packages, since
dependencies between packages play a critical role all along the
process. The following diagram illustrates how complexity arises from
having several levels of dependencies:

.. mermaid::

   graph LR;
   Bundle-->A;
   Bundle-->B;
   B-->C;
   Bundle-->D;
   D-->E;
   E-->F;
   E-->G;
   G-->H;

The packages composing the bundle have themselves dependencies, what
influences a lot how the *integration stage* has to be performed. In the
simplest case, if package A is upgraded, its new version can be selected
in a corresponding branch and a merge request submitted to trigger the
CI. If the pipelines succeed, then the bundle containing the new version
of A can be considered valid. The same holds for package B, as long as
package C is not modified. When a new version of C is uploaded, then the
corresponding branch has to test the whole B-C-Bundle chain because the
global CI pipelines fail if the new version of C breaks B. The
complexity of change validation goes further on with the D sub-tree of
dependencies, the longest chain to validate being H-G-E-D-Bundle. In
practice, something similar happens in the ESL Bundle with the LibGridXC
and ELSI packages.


Time frames
-----------

A new release of the ESL Bundle is published every 6 months, usually one
month before the release of the *foss* and *intel* `reference toolchains of
EasyBuild <https://easybuild.readthedocs.io/en/latest/Common-toolchains.html>`__.
The typical release dates will thus be around June 15 and December 15
each year.

Every time a release is published, a new milestone is defined on the
`Gitlab repository of the ESL
Bundle <https://gitlab.com/ElectronicStructureLibrary/esl-bundle/milestones>`__
for the next release. Proposed changes to the bundle will be discussed
and integrated between the start date and the end date of the milestone,
which usually differ by 5 weeks. These 5 weeks include 2 weeks for
discussions, 2 weeks for the integration of the accepted changes, and 1
buffer week for unexpected issues.

For instance, let's suppose that a new bundle version will be released
on June 17. The discussion stage will thus start on May 13, while the
integration stage will start between May 27 and June 3. On May 13, all
Gitlab issues related to the milestone are collected and the new version
of the ESL Bundle ``README`` file is shared through a new issue where
all stakeholders can discuss the changes. Once the list of accepted /
rejected / postponed changes is agreed upon, the ESL Curating Team helps
the developers of each package get their changes integrated into the
bundle. If everything goes as planned, the new version of the bundle
will be made available whenever all branches have been merged into the
master branch, e.g. June 12, and announced at the scheduled June 17
release date. In case of an unexpected delay, an announcement will be
made by June 14 to inform the users of the situation.
