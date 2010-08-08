Name:           erlang-erlydtl
Version:        0.6.0
Release:        1%{?dist}
Summary:        Erlang implementation of the Django Template Language.

Group:          Development/Libraries
License:        MIT
URL:            http://code.google.com/p/erlydtl/
Source0:        http://erlydtl.googlecode.com/files/erlydtl-0.6.0.tar.gz
Patch0:         erlang-erlydtl-0.6.0-tests.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  erlang
Requires:       erlang

%description
ErlyDTL is an Erlang implementation of the Django Template Language. The
erlydtl module compiles Django Template source code into Erlang bytecode. The
compiled template has a "render" function that takes a list of variables and
returns a fully rendered document. 

%prep
%setup -q -n erlydtl-%{version}

%patch0 -p0

%build
make


%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_libdir}/erlang/lib/erlydtl-%{version}/
cp -r ebin     %{buildroot}/%{_libdir}/erlang/lib/erlydtl-%{version}/
cp -r bin      %{buildroot}/%{_libdir}/erlang/lib/erlydtl-%{version}/
cp -r priv     %{buildroot}/%{_libdir}/erlang/lib/erlydtl-%{version}/


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%{_libdir}/erlang/lib/erlydtl-%{version}/*
%doc README
%doc examples


%changelog
* Sun Aug 1 2010 Ilia Cheishvili <ilia.cheishvili@gmail.com> - 0.6.0-1
- Initial Package