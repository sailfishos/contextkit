# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       contextkit
Summary:    Contextual information collection framework
Version:    0.5.39
Release:    1
Group:      Applications/System
License:    GPLv2
URL:        http://maemo.gitorious.org/maemo-af/%{name}
Source0:    %{name}-%{version}.tar.bz2
Source100:  contextkit.yaml
Patch0:     contextkit-gcc45.patch
Patch1:     contextkit-0.5.39-ignore-docs.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(QJson)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  libxslt
BuildRequires:  python
BuildRequires:  tinycdb-devel


%description
This is ContextKit, a framework for collecting contextual information from
the bowels of the system, cleaning them up and offering them through a simple
API.

The ContextKit consists of:
* libcontextprovider, a convenience library to export contextual properties
  to the rest of the system.
* user documentation including a list of standard context properties.
* contextd, daemon for combining and refining contextual information.
* libcontextsubscriber, a library implementing the simple API for accessing
  the contextual information.



%package devel
Summary:    Development files for ContextKit APIs
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
Development libraries and headers for building context aware applications.


%package -n python-%{name}
Summary:    Python bindings for ContextKit APIs
Group:      Applications/System
Requires:   %{name} = %{version}-%{release}

%description -n python-%{name}
This package contains Python bindings for the libcontextprovider
C interface, which helps you writing providers in Python.


%package tests
Summary:    ContextKit automated customer tests
Group:      Applications/System
Requires:   %{name} = %{version}-%{release}
Requires:   python-%{name} = %{version}-%{release}

%description tests
This package contains an automated customer testsuite of the
ContextKit libraries.



%prep
%setup -q -n %{name}-%{version}

# contextkit-gcc45.patch
%patch0 -p1
# contextkit-0.5.39-ignore-docs.patch
%patch1 -p1
# >> setup
# << setup

%build
# >> build pre
./autogen.sh --no-configure
# << build pre

%configure --disable-static \
    --disable-doc

make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# Fix rpmlint non-executable-script warning
chmod 0755 %{buildroot}%{py_libdir}/site-packages/ContextKit/flexiprovider.py
chmod 0755 %{buildroot}%{py_libdir}/site-packages/ContextKit//cltool.py
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig











%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/dbus-1/system.d/libcontextprovider0.conf
%{_bindir}/update-%{name}-providers
%{_libdir}/libcontextprovider.so.*
%{_libdir}/libcontextsubscriber.so.*
%{_datadir}/%{name}/core.context
%{_datadir}/%{name}/types/core.types
%doc %{_mandir}/man1/update-%{name}-providers.*
# >> files
# << files


%files devel
%defattr(-,root,root,-)
%{_includedir}/contextprovider/*
%{_includedir}/contextsubscriber/*
%{_libdir}/libcontextprovider.so
%{_libdir}/libcontextsubscriber.so
%{_libdir}/pkgconfig/contextprovider-1.0.pc
%{_libdir}/pkgconfig/contextsubscriber-1.0.pc
# >> files devel
# << files devel

%files -n python-%{name}
%defattr(-,root,root,-)
%{_bindir}/context-rlwrap
%{py_libdir}/site-packages/ContextKit/*.py
%exclude %{py_libdir}/site-packages/ContextKit/*.pyc
%exclude %{py_libdir}/site-packages/ContextKit/*.pyo
# >> files python-%{name}
# << files python-%{name}

%files tests
%defattr(-,root,root,-)
%{_bindir}/check-version
%{_bindir}/context-listen
%{_bindir}/context-ls
%{_bindir}/context-provide
%{_libdir}/%{name}/subscriber-test-plugins/contextsubscribertime*.so
%{_datadir}/libcontextsubscriber-tests/regression/context-provide.context
%{_libdir}/libcontextprovider-tests/*
%{_libdir}/libcontextsubscriber-tests/*
%{_datadir}/libcontextprovider-tests/tests.xml
%{_datadir}/libcontextsubscriber-tests/tests.xml
%{_datadir}/libcontextsubscriber-tests/waitforsubscription/context-provide.context
%doc %{_mandir}/man1/context-listen.*
%doc %{_mandir}/man1/context-ls.*
%doc %{_mandir}/man1/context-provide.*
# >> files tests
# << files tests

