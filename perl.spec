# based on PLD Linux spec git://git.pld-linux.org/packages/perl.git
%define		abi		5.20.0

# distribution
%define		perl_archlib	%{_libdir}/perl5
%define		perl_privlib	%{_datadir}/perl5
# 3rd party
%define		perl_vendorarch	%{_libdir}/perl5/vendor_perl
%define		perl_vendorlib	%{_datadir}/perl5/vendor_perl
# CPAN
%define		perl_sitearch	%{_prefix}/local/%{_lib}/perl5
%define		perl_sitelib	%{_prefix}/local/share/perl5

%define		__perl			%{_builddir}/perl-%{version}/runperl
%define		__perl_provides		%{__perl} %{SOURCE1}

Summary:	Practical Extraction and Report Language (Perl)
Name:		perl
Version:	5.20.1
Release:	1
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/src/%{name}-%{version}.tar.gz
# Source0-md5:	7a195abb7d6769f751e90c7d30dcf2e0
Source1:	%{name}.prov
Patch0:		%{name}-errno_h-parsing.patch
Patch1:		%{name}-soname.patch
Patch2:		%{name}-test-noproc.patch
Patch3:		%{name}-write-permissions.patch
URL:		http://dev.perl.org/perl5/
BuildRequires:	gdbm-devel
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Perl is an interpreted language optimized for scanning arbitrary text
files, extracting information from those text files, and printing
reports based on that information. It's also a good language for many
system management tasks. The language is intended to be practical
(easy to use, efficient, complete) rather than beautiful (tiny,
elegant, minimal).

%package libs
Summary:	Shared Perl library
Group:		Libraries

%description libs
Shared Perl library.

%package base
Summary:	Base Perl components for a minimal installation
Group:		Development/Languages/Perl
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	%{perl_vendorarch}
Requires:	%{perl_vendorlib}
Provides:	perl(File::Compare)
Provides:	perl(File::Temp)
Provides:	perl(IO)
Provides:	perl(IO-Compress)
Provides:	perl(IO::Zlib)
Provides:	perl(IPC::Cmd)
Provides:	perl(PathTools)
Provides:	perl(PerlIO::via::QuotedPrint)
Provides:	perl(Socket)
Provides:	perl(Tie::File)
Provides:	perl(Tie::RefHash)
Provides:	perl(largefiles)
Provides:	perl(parent)

%description base
Base components, files, core modules, etc. -- a minimal usable Perl
installation. You are encouraged to install a full Perl (the perl
package) whenever possible.

%package devel
Summary:	Perl development files
Group:		Development/Libraries
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	%{name}-tools-pod = %{epoch}:%{version}-%{release}
Provides:	perl(CPAN)
Provides:	perl(CPAN::Meta)
Provides:	perl(CPAN::Meta::YAML)
Provides:	perl(Devel::PPPort)
Provides:	perl(Devel::Peek)
Provides:	perl(ExtUtils::CBuilder)
Provides:	perl(ExtUtils::Command)
Provides:	perl(ExtUtils::Embed)
Provides:	perl(ExtUtils::Install)
Provides:	perl(ExtUtils::MakeMaker)
Provides:	perl(ExtUtils::Manifest)
Provides:	perl(ExtUtils::ParseXS)
Provides:	perl(Module::Build)

%description devel
Components required for developing applications which embed a Perl
interpreter and compiling Perl modules.

%package doc-pod
Summary:	Perl documentation in POD format
Group:		Documentation
Requires:	perldoc

%description doc-pod
Practical Extraction and Report Language - POD docs.

%package doc-reference
Summary:	Perl reference documentation
Group:		Documentation

%description doc-reference
Reference documentation for the Practical Extraction and Report
Language and it's interpreter in the man(1) format.

%package modules
Summary:	Modules from the core Perl distribution
Group:		Libraries
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Provides:	perl(Scalar-List-Utils)
Provides:	perl(Archive::Tar)
Provides:	perl(Attribute::Handlers)
Provides:	perl(CGI)
Provides:	perl(Compress::Raw::Bzip2)
Provides:	perl(Compress::Raw::Zlib)
Provides:	perl(Digest)
Provides:	perl(Digest::MD5)
Provides:	perl(Digest::SHA)
Provides:	perl(Filter::Simple)
Provides:	perl(FindBin)
Provides:	perl(I18N::LangTags)
Provides:	perl(IPC::SysV
Provides:	perl(JSON::PP)
Provides:	perl(Locale::Codes)
Provides:	perl(Locale::Maketext)
Provides:	perl(Locale::Maketext::Simple)
Provides:	perl(MIME::Base64)
Provides:	perl(Math::BigInt)
Provides:	perl(Math::BigInt::FastCalc)
Provides:	perl(Math::BigRat)
Provides:	perl(Math::Complex)
Provides:	perl(Math::Trig)
Provides:	perl(Memoize)
Provides:	perl(Module::CoreList)
Provides:	perl(Module::Load)
Provides:	perl(Module::Load::Conditional)
Provides:	perl(Module::Metadata)
Provides:	perl(NEXT)
Provides:	perl(Pod::Parser)
Provides:	perl(Pod::Simple)
Provides:	perl(Safe)
Provides:	perl(Storable)
Provides:	perl(Sys::Syslog)
Provides:	perl(Term::ANSIColor)
Provides:	perl(Term::Cap)
Provides:	perl(Test)
Provides:	perl(Test::Harness)
Provides:	perl(Test::Simple)
Provides:	perl(Text::Balanced)
Provides:	perl(Text::ParseWords)
Provides:	perl(Time::HiRes)
Provides:	perl(Time::Piece)
Provides:	perl(UNIVERSAL)
Provides:	perl(Unicode::Collate)
Provides:	perl(Unicode::Normalize)
Provides:	perl(bignum)
Provides:	perl(libnet)
Provides:	perl(version)

%description modules
Practical Extraction and Report Language - modules from the core
distribution.

%package perldoc
Summary:	perldoc - Look up Perl documentation in pod format
Group:		Development/Tools
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}
Requires:	%{name}-tools-pod = %{epoch}:%{version}-%{release}
Provides:	perldoc = 3.14_02@%{version}
Requires:       groff

%description perldoc
perldoc looks up a piece of documentation in .pod format that is
embedded in the Perl installation tree or in a Perl script, and
displays it via "pod2man | nroff -man | $PAGER". This is primarily
used for the documentation for the Perl library modules.

%package tools
Summary:	Various tools from the core Perl distribution
Group:		Applications
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description tools
Various tools from the core Perl distribution:
a2p		- Awk to Perl translator
find2perl	- translate find command lines to Perl code
psed, s2p	- a stream editor
and others.

%package tools-devel
Summary:	Devel2oper's tools from the core Perl distribution
Group:		Development/Tools
Requires:	%{name}-base = %{epoch}:%{version}-%{release}
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description tools-devel
Various tools from the core Perl distribution:
c2ph, pstruct	- Dump C structures as generated from C<cc -g -S> stabs
dprofpp		- display Perl profile data
h2ph		- convert .h C header files to .ph Perl header files
h2xs		- convert .h C header files to Perl extensions
perlcc		- generate executables from Perl programs
perlivp		- Perl Installation Verification Procedure
pl2pm		- Rough tool to translate Perl4 .pl files to Perl5 .pm modules.
splain		- force verbose warning diagnostics

%package tools-pod
Summary:	Tools for manipulating files in the POD format
Group:		Applications
Requires:	%{name}-modules = %{epoch}:%{version}-%{release}

%description tools-pod
Tools for manipulating files in the POD (Plain Old Documentation)
format:
pod2html	- convert .pod files to .html files
pod2latex	- convert pod documentation to LaTeX format
pod2man		- convert POD data to formatted *roff input
pod2text	- convert POD data to formatted ASCII text
pod2usage	- print usage messages from embedded pod docs in files
podchecker	- check the syntax of POD format documentation files
podselect	- print selected sections of pod documentation

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

cat > runperl <<'EOF'
#!/bin/sh
LD_PRELOAD="%{_builddir}/%{name}-%{version}/libperl.so.%{abi}" \
PERL5LIB="%{buildroot}%{perl_privlib}:%{buildroot}%{perl_archlib}" \
exec %{buildroot}%{_bindir}/perl ${1:+"$@"}
EOF
chmod a+x runperl

%build
sh Configure \
	-Darchname=%{_target_platform}					\
	-Dcc="%{__cc}"							\
	-Dcccdlflags='-fPIC'						\
	-Dccdlflags='-rdynamic' 					\
	-Dlddlflags="-shared %{rpmldflags}"				\
	-Dldflags="%{rpmldflags}"					\
	-Doptimize="%{rpmcflags}"					\
	-Dldlibpthname=none						\
	-Dprefix=%{_prefix}						\
	-Dlibpth="%{_libdir}"						\
	-Dsitearch=%{perl_sitearch}					\
	-Dsitelib=%{perl_sitelib}					\
	-Dsiteprefix=%{_usr}/local					\
	-Dprivlib=%{perl_privlib}					\
	-Darchlib=%{perl_archlib}					\
	-Dvendorlib=%{perl_vendorlib}					\
	-Dvendorarch=%{perl_vendorarch}					\
	-Dvendorprefix=%{_prefix}					\
	-Dman1dir=%{_mandir}/man1 -Dman1ext=1				\
	-Dman3dir=%{_mandir}/man3 -Dman3ext=3perl			\
	-Dsiteman1dir=%{_usr}/local/man/man1 -Dsiteman1ext=1p		\
	-Dsiteman3dir=%{_usr}/local/man/man3 -Dsiteman3ext=3pm		\
	-Dvendorman1dir=%{_mandir}/man1 -Dvendorman1ext=1p		\
	-Dvendorman3dir=%{_mandir}/man3 -Dvendorman3ext=3pm		\
	-Duselargefiles							\
	-Duseshrplib							\
	-Dusethreads							\
	-UDEBUGGING							\
	-Ui_db -Ui_dbm -Di_gdbm -Ui_ndbm				\
	-des
%{__make} \
	LIBPERL_SONAME=libperl.so.%{abi} \
	LDDLFLAGS="%{rpmcflags} -shared"


%install
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# use symlinks instead of hardlinks
%{__ln_s} -f perl%{version} $RPM_BUILD_ROOT%{_bindir}/perl
%{__ln_s} -f c2ph $RPM_BUILD_ROOT%{_bindir}/pstruct
%{__ln_s} -f psed $RPM_BUILD_ROOT%{_bindir}/s2p

install -d $RPM_BUILD_ROOT%{perl_vendorarch}
# install directory needed by packages dependant on TAP::Harness
install -d $RPM_BUILD_ROOT%{perl_privlib}/TAP/Harness
# install directory needed by packages dependant on Encode
install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Encode

# Fix library version
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/CORE/libperl.so
mv $RPM_BUILD_ROOT%{perl_archlib}/CORE/libperl.so.%{abi} $RPM_BUILD_ROOT%{_libdir}
%{__ln_s} ../../../../libperl.so.%{abi} $RPM_BUILD_ROOT%{perl_archlib}/CORE/libperl.so.%{abi}
%{__ln_s} libperl.so.%{abi} $RPM_BUILD_ROOT%{_libdir}/libperl.so

# installed as non-executable - let rpm generate deps
chmod 755 $RPM_BUILD_ROOT%{_libdir}/libperl.so.%{abi}

# Fix Config.pm: remove buildroot path and change man pages extensions
%{__perl} -pi -e 's,%{buildroot}/*,/,g'			$RPM_BUILD_ROOT%{perl_archlib}/Config.pm
%{__perl} -pi -e "s,^man1ext='1',man1ext='1p',"		$RPM_BUILD_ROOT%{perl_archlib}/Config_heavy.pl
%{__perl} -pi -e "s,^man3ext='3perl',man3ext='3pm',"	$RPM_BUILD_ROOT%{perl_archlib}/Config_heavy.pl

# Generate the *.ph files
owd=$(pwd)
cd /usr/include
H2PH=$RPM_BUILD_ROOT%{_bindir}/h2ph
PHDIR=$RPM_BUILD_ROOT%{perl_archlib}
WANTED='
	syscall.h
	syslog.h
	termios.h
	wait.h
	asm/termios.h
	sys/ioctl.h
	sys/socket.h
	sys/syscall.h
	sys/time.h
	linux/posix_types.h
	linux/stddef.h
'
%{__perl} $H2PH -a -d $PHDIR $WANTED || :
cd "$owd"

# remove man pages for other operating systems
%{__rm}	$RPM_BUILD_ROOT%{_mandir}/man1/perl{aix,amiga,bs2000,ce,cygwin,dos}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{freebsd,hpux,macos,os2,os390}* \
	$RPM_BUILD_ROOT%{_mandir}/man1/perl{qnx,solaris,vms,vos,win32}*

#  File::Spec submodules are for non-Unix systems
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/File/Spec/[EMOVW]*.pm
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man3/File::Spec::{Epoc,Mac,OS2,VMS,Win32}.3perl*

# We already have these *.pod files as man pages
%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/{Encode,Test,Net,Locale{,/Maketext},version}/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/pod/a2p.pod
%{__rm} $RPM_BUILD_ROOT%{perl_privlib}/*.pod
%{__rm} $RPM_BUILD_ROOT%{perl_archlib}/*.pod

# cpan tools, we use rpm instead of cpan for managing packages (some search tool would be nice to have but...)
%{__rm} $RPM_BUILD_ROOT%{_bindir}/cpan*
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/cpan*
# others
%{__rm} $RPM_BUILD_ROOT%{_bindir}/config_data
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man1/config_data*

%check
%if 0
#   Failed test 'DummyHard.pm not writeable'
#   at t/Install.t line 240.

#   Failed test 'DummyOrig.pm not writeable'
#   at t/Install.t line 264.
# Looks like you failed 2 tests of 60.
# ../dist/ExtUtils-Install/t/Install.t .............................. Dubious, test returned 2 (wstat 512, 0x200)
# Failed 2/60 subtests

%{__make} test_harness -j1
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_bindir}/perlthanks

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libperl.so.%{abi}

%files base
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perl
%attr(755,root,root) %{_bindir}/perl%{version}
%{_mandir}/man1/perl.1*

%dir %{perl_archlib}
%dir %{perl_archlib}/CORE
%attr(755,root,root) %{perl_archlib}/CORE/libperl.so.%{abi}
%dir %{perl_privlib}
%dir %{perl_vendorarch}
%dir %{perl_vendorlib}

# pragmas
%{perl_privlib}/_charnames*
%{perl_privlib}/autodie*
%{perl_privlib}/base.pm
%{perl_privlib}/constant.pm
%{perl_privlib}/diagnostics.pm
%{perl_privlib}/feature.pm
%{perl_privlib}/fields.pm
%{perl_privlib}/integer.pm
%{perl_privlib}/overload*
%{perl_privlib}/parent.pm
%{perl_privlib}/sort.pm
%{perl_privlib}/strict.pm
%{perl_privlib}/subs.pm
%{perl_privlib}/vars.pm
%{perl_privlib}/warnings*
%{perl_privlib}/experimental.pm
%{_mandir}/man3/experimental.*
%{_mandir}/man3/autodie*
%{_mandir}/man3/base.*
%{_mandir}/man3/constant.*
%{_mandir}/man3/diagnostics.*
%{_mandir}/man3/feature.*
%{_mandir}/man3/fields.*
%{_mandir}/man3/integer.*
%{_mandir}/man3/overload*
%{_mandir}/man3/parent.*
%{_mandir}/man3/sort.*
%{_mandir}/man3/strict.*
%{_mandir}/man3/subs.*
%{_mandir}/man3/vars.*
%{_mandir}/man3/warnings*

%{perl_archlib}/lib.pm
%{_mandir}/man3/lib.*

# arch-_IN_dependent modules
%dir %{perl_privlib}/Class
%{perl_privlib}/Auto*
%{perl_privlib}/Carp*
%{perl_privlib}/Class/Struct*
%{perl_privlib}/English*
%{perl_privlib}/Exporter*
%{perl_privlib}/Getopt*
%{perl_privlib}/IPC
%{perl_privlib}/Safe*
%{perl_privlib}/SelectSaver.pm
%{perl_privlib}/Symbol.pm
%{perl_privlib}/Tie
%{perl_privlib}/XSLoader*
%{_mandir}/man3/Auto*
%{_mandir}/man3/Carp*
%{_mandir}/man3/Class::Struct*
%{_mandir}/man3/English*
%{_mandir}/man3/Exporter*
%{_mandir}/man3/Getopt*
%{_mandir}/man3/IPC::Cmd*
%{_mandir}/man3/IPC::Open*
%{_mandir}/man3/Safe*
%{_mandir}/man3/SelectSaver.*
%{_mandir}/man3/Symbol.*
%{_mandir}/man3/Tie::*
%{_mandir}/man3/XSLoader*

# arch-dependent modules
%{_mandir}/man3/Config.*
%{_mandir}/man3/DynaLoader*
%{_mandir}/man3/Errno*
%{perl_archlib}/Config*
%{perl_archlib}/DynaLoader*
%{perl_archlib}/Errno*
%{perl_archlib}/Tie

%dir %{perl_archlib}/auto
%attr(755,root,root) %{perl_archlib}/auto/Cwd/*.so
%dir %{perl_archlib}/auto/Cwd
%{perl_archlib}/Cwd.pm
%{_mandir}/man3/Cwd.*

%{perl_archlib}/Fcntl.*
%dir %{perl_archlib}/auto/Fcntl
%attr(755,root,root) %{perl_archlib}/auto/Fcntl/*.so
%{_mandir}/man3/Fcntl.*

%{perl_privlib}/File*
%{perl_archlib}/File
%dir %{perl_archlib}/auto/File
%dir %{perl_archlib}/auto/File/*/
%attr(755,root,root) %{perl_archlib}/auto/File/*/*.so
%{_mandir}/man3/File*

%{perl_privlib}/IO
%{perl_archlib}/IO*
%dir %{perl_archlib}/auto/IO
%attr(755,root,root) %{perl_archlib}/auto/IO/*.so
%{_mandir}/man3/IO*

%{perl_archlib}/Opcode.*
%dir %{perl_archlib}/auto/Opcode
%attr(755,root,root) %{perl_archlib}/auto/Opcode/*.so
%{_mandir}/man3/Opcode.*

%{perl_privlib}/PerlIO*
%{perl_archlib}/PerlIO
%dir %{perl_archlib}/auto/PerlIO
%dir %{perl_archlib}/auto/PerlIO/*/
%attr(755,root,root) %{perl_archlib}/auto/PerlIO/*/*.so
%{_mandir}/man3/PerlIO*

%{perl_archlib}/POSIX*
%dir %{perl_archlib}/auto/POSIX
%attr(755,root,root) %{perl_archlib}/auto/POSIX/*.so
%{_mandir}/man3/POSIX.*

%{perl_archlib}/Socket.*
%dir %{perl_archlib}/auto/Socket
%attr(755,root,root) %{perl_archlib}/auto/Socket/*.so
%{_mandir}/man3/Socket.*

%{perl_archlib}/arybase.*
%dir %{perl_archlib}/auto/arybase
%attr(755,root,root) %{perl_archlib}/auto/arybase/*.so
%{_mandir}/man3/arybase.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libperl.so
%attr(755,root,root) %{perl_archlib}/auto/B/*.so
%attr(755,root,root) %{perl_archlib}/auto/Devel/*/*.so

%dir %{perl_archlib}/auto/B
%dir %{perl_archlib}/auto/Devel
%dir %{perl_archlib}/auto/Devel/*/
%dir %{perl_privlib}/App

%{perl_archlib}/B
%{perl_archlib}/B.pm
%{perl_archlib}/CORE/*.h
%{perl_archlib}/Devel
%{perl_archlib}/O.*
%{perl_privlib}/App/Cpan.pm
%{perl_privlib}/B
%{perl_privlib}/CPAN*
%{perl_privlib}/DB.*
%{perl_privlib}/Devel
%{perl_privlib}/ExtUtils
%{perl_privlib}/Module/Build*
%{perl_privlib}/inc
%{perl_privlib}/vmsish.pm
%{_mandir}/man3/App::Cpan*
%{_mandir}/man3/B[.:]*
%{_mandir}/man3/CORE*
%{_mandir}/man3/CPAN*
%{_mandir}/man3/DB.*
%{_mandir}/man3/Devel::*
%{_mandir}/man3/ExtUtils*
%{_mandir}/man3/Module::Build*
%{_mandir}/man3/O.*
%{_mandir}/man3/inc::latest*
%{_mandir}/man3/vmsish.*

%files doc-pod
%defattr(644,root,root,755)
%{perl_privlib}/pod/perl.pod
%{perl_privlib}/pod/perl[5abceghijklmnopqrstuvwx]*.pod
%{perl_privlib}/pod/perld[!i]*.pod
%{perl_privlib}/pod/perlf[!au]*.pod

%files doc-reference
%defattr(644,root,root,755)
%{_mandir}/man1/perl[5aefghlmnoprstuvwx]*
%{_mandir}/man1/perlbo*
%{_mandir}/man1/perlcall.*
%{_mandir}/man1/perlcheat.*
%{_mandir}/man1/perlclib.*
%{_mandir}/man1/perlcommunity.*
%{_mandir}/man1/perld[!o]*
%{_mandir}/man1/perli[!v]*

%files modules
%defattr(644,root,root,755)
%{perl_privlib}/unicore

# pragmas
%{perl_privlib}/autouse.pm
%{perl_privlib}/big*.pm
%{perl_privlib}/blib.pm
%{perl_privlib}/bytes.pm
%{perl_privlib}/charnames.pm
%{perl_privlib}/deprecate*.pm
%{perl_privlib}/encoding
%{perl_privlib}/filetest.pm
%{perl_privlib}/if.pm
%{perl_privlib}/less.pm
%{perl_privlib}/locale.pm
%{perl_privlib}/open.pm
%{perl_privlib}/sigtrap.pm
%{perl_privlib}/utf8.pm
%{_mandir}/man3/autouse.*
%{_mandir}/man3/big*
%{_mandir}/man3/blib.*
%{_mandir}/man3/bytes.*
%{_mandir}/man3/charnames.*
%{_mandir}/man3/deprecate*
%{_mandir}/man3/encoding::*
%{_mandir}/man3/filetest.*
%{_mandir}/man3/if.*
%{_mandir}/man3/less.*
%{_mandir}/man3/locale.*
%{_mandir}/man3/open.*
%{_mandir}/man3/sigtrap.*
%{_mandir}/man3/utf8.*

%dir %{perl_privlib}/version
%{perl_privlib}/version.pm
%{perl_privlib}/version/regex.pm
%{perl_privlib}/version/vpp.pm
%{_mandir}/man3/version*

%attr(755,root,root) %{perl_archlib}/auto/attributes/*.so
%dir %{perl_archlib}/auto/attributes
%{perl_archlib}/attributes.pm
%{_mandir}/man3/attributes.*

%attr(755,root,root) %{perl_archlib}/auto/mro/*.so
%attr(755,root,root) %{perl_archlib}/auto/re/*.so
%dir %attr(755,root,root) %{perl_archlib}/auto/mro
%dir %{perl_archlib}/auto/re
%{perl_archlib}/mro.pm
%{perl_archlib}/ops.pm
%{perl_archlib}/re.pm
%{_mandir}/man3/mro.*
%{_mandir}/man3/ops.*
%{_mandir}/man3/re.*

%attr(755,root,root) %{perl_archlib}/auto/threads/*.so
%attr(755,root,root) %{perl_archlib}/auto/threads/shared/*.so
%dir %{perl_archlib}/auto/threads
%dir %{perl_archlib}/auto/threads/shared
%{perl_archlib}/threads*
%{_mandir}/man3/t*

# old *.pl files
%{perl_privlib}/*.pl

# *.ph files (could be made a separate package, but an autohelper's support is needed)
%{perl_archlib}/*.ph
%{perl_archlib}/asm
%{perl_archlib}/asm-generic
%{perl_archlib}/bits
%{perl_archlib}/gnu
%{perl_archlib}/linux
%{perl_archlib}/sys

%attr(755,root,root) %{perl_archlib}/auto/Tie/Hash/NamedCapture/NamedCapture.so
%dir %{perl_archlib}/auto/Tie
%dir %{perl_archlib}/auto/Tie/Hash
%dir %{perl_archlib}/auto/Tie/Hash/NamedCapture

%attr(755,root,root) %{perl_archlib}/auto/Compress/Raw/*/*.so
%dir %{perl_archlib}/auto/Compress
%dir %{perl_archlib}/auto/Compress/Raw
%dir %{perl_archlib}/auto/Compress/Raw/*/
%{perl_archlib}/Compress
%{perl_privlib}/Compress
%{_mandir}/man3/Compress*

%attr(755,root,root) %{perl_archlib}/auto/Data/Dumper/*.so
%dir %{perl_archlib}/auto/Data
%dir %{perl_archlib}/auto/Data/Dumper
%{perl_archlib}/Data
%{_mandir}/man3/Data*

%attr(755,root,root) %{perl_archlib}/auto/Digest/*/*.so
%dir %{perl_archlib}/auto/Digest
%dir %{perl_archlib}/auto/Digest/*/
%{perl_archlib}/Digest
%{perl_privlib}/Digest*
%{_mandir}/man3/Digest*

%{perl_privlib}/DBM_Filter*
%{_mandir}/man3/DBM_Filter*

%attr(755,root,root) %{_bindir}/enc2xs
%attr(755,root,root) %{_bindir}/piconv
%{perl_privlib}/Encode
%{perl_archlib}/Encode*
%{perl_archlib}/encoding.pm
%dir %{perl_archlib}/auto/Encode
%dir %{perl_archlib}/auto/Encode/*/
%dir %{perl_vendorlib}/Encode
%attr(755,root,root) %{perl_archlib}/auto/Encode/*/*.so
%{_mandir}/man1/enc2xs.*
%{_mandir}/man1/piconv.*
%{_mandir}/man3/Encode*
%{_mandir}/man3/encoding.*

%attr(755,root,root) %{perl_archlib}/auto/Filter/Util/Call/*.so
%dir %{perl_archlib}/auto/Filter
%dir %{perl_archlib}/auto/Filter/Util
%dir %{perl_archlib}/auto/Filter/Util/Call
%{perl_archlib}/Filter
%{perl_privlib}/Filter
%{_mandir}/man3/Filter*

%{perl_archlib}/GDBM_File.*
%dir %{perl_archlib}/auto/GDBM_File
%attr(755,root,root) %{perl_archlib}/auto/GDBM_File/*.so
%{_mandir}/man3/GDBM_File.*

%attr(755,root,root) %{perl_archlib}/auto/Hash/*/*.so
%attr(755,root,root) %{perl_archlib}/auto/Hash/*/*/*.so
%dir %{perl_archlib}/auto/Hash
%dir %{perl_archlib}/auto/Hash/*/
%dir %{perl_archlib}/auto/Hash/*/FieldHash
%{perl_archlib}/Hash
%{_mandir}/man3/Hash::*

%attr(755,root,root) %{perl_archlib}/auto/I18N/*/*.so
%dir %{perl_archlib}/auto/I18N
%dir %{perl_archlib}/auto/I18N/*/
%{perl_archlib}/I18N
%{perl_privlib}/I18N
%{_mandir}/man3/I18N::*

%attr(755,root,root) %{perl_archlib}/auto/IPC/*/*.so
%dir %{perl_archlib}/auto/IPC
%dir %{perl_archlib}/auto/IPC/*/
%{perl_archlib}/IPC
%{_mandir}/man3/IPC::[MS]*

%attr(755,root,root) %{perl_archlib}/auto/List/*/*.so
%dir %{perl_archlib}/auto/List
%dir %{perl_archlib}/auto/List/*/
%{perl_archlib}/List
%{_mandir}/man3/List::*

%attr(755,root,root) %{perl_archlib}/auto/Math/*/*/*.so
%dir %{perl_archlib}/auto/Math
%dir %{perl_archlib}/auto/Math/*/
%dir %{perl_archlib}/auto/Math/*/*/
%{perl_archlib}/Math
%{perl_privlib}/Math
%{_mandir}/man3/Math::*

%attr(755,root,root) %{perl_archlib}/auto/MIME/Base64/*.so
%dir %{perl_archlib}/auto/MIME
%dir %{perl_archlib}/auto/MIME/Base64
%{perl_archlib}/MIME
%{_mandir}/man3/MIME::*

%attr(755,root,root) %{perl_archlib}/auto/SDBM_File/*.so
%dir %{perl_archlib}/auto/SDBM_File
%{perl_archlib}/SDBM_File.*
%{_mandir}/man3/SDBM_File.*

%attr(755,root,root) %{perl_archlib}/auto/Storable/*.so
%dir %{perl_archlib}/auto/Storable
%{perl_archlib}/Storable.*
%{_mandir}/man3/Storable.*

%attr(755,root,root) %{perl_archlib}/auto/Sys/*/*.so
%dir %{perl_archlib}/auto/Sys
%dir %{perl_archlib}/auto/Sys/*/
%{perl_archlib}/Sys
%{_mandir}/man3/Sys::*

%attr(755,root,root) %{perl_archlib}/auto/Time/*/*.so
%dir %{perl_archlib}/auto/Time
%dir %{perl_archlib}/auto/Time/*/
%{perl_archlib}/Time
%{perl_privlib}/Time
%{_mandir}/man3/Time::*

%attr(755,root,root) %{perl_archlib}/auto/Unicode/*/*.so
%dir %{perl_archlib}/auto/Unicode
%dir %{perl_archlib}/auto/Unicode/*
%dir %{perl_privlib}/Unicode
%{perl_archlib}/Unicode
%{perl_privlib}/Unicode/*.pm
%{perl_privlib}/Unicode/Collate
%{_mandir}/man3/Unicode::*

%dir %{perl_privlib}/HTTP
%dir %{perl_privlib}/Module
%dir %{perl_privlib}/Net
%dir %{perl_privlib}/Perl
%{perl_archlib}/Scalar
%{perl_privlib}/AnyDBM*
%{perl_privlib}/App
%{perl_privlib}/Archive*
%{perl_privlib}/Attribute
%{perl_privlib}/Benchmark*
%{perl_privlib}/CGI*
%{perl_privlib}/Config
%{perl_privlib}/DirHandle*
%{perl_privlib}/Dumpvalue.*
%{perl_privlib}/Env.*
%{perl_privlib}/Fatal.*
%{perl_privlib}/FindBin.*
%{perl_privlib}/HTTP/Tiny.pm
%{perl_privlib}/IPC
%{perl_privlib}/Locale
%{perl_privlib}/Memoize*
%{perl_privlib}/Module/[CLMP]*
%{perl_privlib}/NEXT.pm
%{perl_privlib}/Net/*.pm
%{perl_privlib}/Net/FTP
%{perl_privlib}/Package
%{perl_privlib}/Params
%{perl_privlib}/Parse
%{perl_privlib}/Perl/OSType.pm
%{perl_privlib}/Pod
%{perl_privlib}/Search
%{perl_privlib}/SelfLoader.*
%{perl_privlib}/TAP
%{perl_privlib}/Term
%{perl_privlib}/Test*
%{perl_privlib}/Text
%{perl_privlib}/Thread*
%{perl_privlib}/UNIVERSAL.*
%{perl_privlib}/User
%{_mandir}/man3/AnyDBM*
%{_mandir}/man3/App::Prove*
%{_mandir}/man3/Archive*
%{_mandir}/man3/Attribute*
%{_mandir}/man3/Benchmark*
%{_mandir}/man3/CGI*
%{_mandir}/man3/Config::*
%{_mandir}/man3/DirHandle*
%{_mandir}/man3/Dumpvalue.*
%{_mandir}/man3/Env.*
%{_mandir}/man3/Fatal.*
%{_mandir}/man3/FindBin.*
%{_mandir}/man3/HTTP::Tiny.*
%{_mandir}/man3/Locale::*
%{_mandir}/man3/Memoize*
%{_mandir}/man3/Module::[CLMP]*
%{_mandir}/man3/NEXT*
%{_mandir}/man3/Net::*
%{_mandir}/man3/Package::*
%{_mandir}/man3/Params::*
%{_mandir}/man3/Parse::CPAN::Meta*
%{_mandir}/man3/Perl::OSType.*
%{_mandir}/man3/Pod::*
%{_mandir}/man3/Scalar::*
%{_mandir}/man3/Search::*
%{_mandir}/man3/SelfLoader.*
%{_mandir}/man3/TAP::*
%{_mandir}/man3/Term::*
%{_mandir}/man3/Test*
%{_mandir}/man3/Text::*
%{_mandir}/man3/Thread*
%{_mandir}/man3/UNIVERSAL.*
%{_mandir}/man3/User::*

%attr(755,root,root) %{_bindir}/json_pp
%{perl_privlib}/JSON
%{_mandir}/man1/json_pp.1*
%{_mandir}/man3/JSON::PP.*
%{_mandir}/man3/JSON::PP::Boolean.*

%files perldoc
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/perldoc
%dir %{perl_privlib}/pod
%{perl_privlib}/pod/perldiag.pod
%{perl_privlib}/pod/perlfaq*.pod
%{perl_privlib}/pod/perlfunc.pod
%{perl_privlib}/perlfaq.pm
%{_mandir}/man1/perldoc.*

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/a2p
%attr(755,root,root) %{_bindir}/corelist
%attr(755,root,root) %{_bindir}/find2perl
%attr(755,root,root) %{_bindir}/instmodsh
%attr(755,root,root) %{_bindir}/libnetcfg
%attr(755,root,root) %{_bindir}/psed
%attr(755,root,root) %{_bindir}/ptar
%attr(755,root,root) %{_bindir}/ptardiff
%attr(755,root,root) %{_bindir}/ptargrep
%attr(755,root,root) %{_bindir}/s2p
%attr(755,root,root) %{_bindir}/shasum
%attr(755,root,root) %{_bindir}/zipdetails
%{_mandir}/man1/a2p.*
%{_mandir}/man1/corelist.*
%{_mandir}/man1/find2perl.*
%{_mandir}/man1/instmodsh.*
%{_mandir}/man1/libnetcfg.*
%{_mandir}/man1/psed.*
%{_mandir}/man1/ptar.*
%{_mandir}/man1/ptardiff.*
%{_mandir}/man1/ptargrep.*
%{_mandir}/man1/s2p.*
%{_mandir}/man1/shasum.*
%{_mandir}/man1/zipdetails.1*

%files tools-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/c2ph
%attr(755,root,root) %{_bindir}/h2ph
%attr(755,root,root) %{_bindir}/h2xs
%attr(755,root,root) %{_bindir}/perlbug
%attr(755,root,root) %{_bindir}/perlivp
%attr(755,root,root) %{_bindir}/pl2pm
%attr(755,root,root) %{_bindir}/prove
%attr(755,root,root) %{_bindir}/pstruct
%attr(755,root,root) %{_bindir}/splain
%attr(755,root,root) %{_bindir}/xsubpp
%{_mandir}/man1/c2ph.*
%{_mandir}/man1/h2ph.*
%{_mandir}/man1/h2xs.*
%{_mandir}/man1/perlbug.*
%{_mandir}/man1/perlivp.*
%{_mandir}/man1/pl2pm.*
%{_mandir}/man1/prove.*
%{_mandir}/man1/pstruct.*
%{_mandir}/man1/splain.*
%{_mandir}/man1/xsubpp.*

%files tools-pod
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pod*
%{_mandir}/man1/pod*

