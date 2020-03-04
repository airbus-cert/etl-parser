# etl-parser
Event Trace Log file reader in pure Python

`etl-parser` is a pure Python 3 parser library for `ETL` Windows log files. `ETL` is the default format for [ETW](https://docs.microsoft.com/en-us/windows/win32/etw/event-tracing-portal) as well as the default format for the Kernel logger.

`etl-parser` has no system dependencies, and will work well on both Windows and Linux.

Since this format is not documented, we merged information from the blog of [Geoff Chappel](https://www.geoffchappell.com/) and reverse engineering activities conducted by Airbus CERT team.

What is `ETL` and why is it a pain to work with? Consider `ETL` as a container, like `AVI` is for video files. Reading `ETL` is similarly frustrating as reading an `AVI` file without the right codec.

`etl-parser` tries to solve this problem by including parsers for the following well known log formats:
* ETW manifest base provider
* TraceLogging
* MOF for kernel log

## How to use `etl-parser`?

`etl-parser` offers two scripts.
The first script, `etl2xml` transforms all known ETL events into XML:

```
etl2xml -i example.etl -o example.xml
```

The second script, `etl2pcap` transforms network captures created through `netsh` into the `pcap` file format:

```
netsh start trace capture=yes
netsh stop trace

etl2pcap -i NetTrace.etl -o NetTrace.pcap
```

You can also use `etl-parser` as a library:

```python
from etl.etl import IEtlFileObserver, build_from_stream
from etl.system import SystemTraceRecord
from etl.perf import PerfInfo
from etl.event import Event
from etl.trace import Trace
from etl.wintrace import WinTrace

class EtlFileLogger(IEtlFileObserver):
    def on_system_trace(self, event: SystemTraceRecord):
        """Mof kernel message with Process Id and Thread Id"""
        mof = event.get_mof() # Invoke MOF parser

    def on_perfinfo_trace(self, event: PerfInfo):
        """Mof kernel message with timestamp"""
        mof = event.get_mof() # Invoke MOF parser

    def on_trace_record(self, event: Trace):
        """unknown"""

    def on_event_record(self, event: Event):
        """ETW event this is what you search"""
        message = event.parse_tracelogging() # Invoke TraceLogging parser
        message = event.parse_etw() # Invoke Manifest based parser

    def on_win_trace(self, event: WinTrace):
        """unknown"""
        etw = event.parse_etw()

with open("example.etl") as etl_file:
    etl_reader = build_from_stream(etl_file.read())
    etl_reader.parse(EtlFileLogger())
```

# Installation

`etl-parser` is available from pip:

```
pip install etl-parser
```

Alternatively, you can install `etl-parser` using `setup.py`:

```
git clone https://github.com/airbus-cert/etl-parser.git
cd etl-parser
pip install -e .
```

## Missing a parser?

If you encounter a parsing error, please open an issue on the Airbus CERT GitHub repository.

## Why an ETL Parser?

The `EVTX` log format is fairly well documented, with lots of libraries and tools available today. This is not true for `ETL`: at time of development, there is no significant open-source project that we know of and the `ETL` format is not well documented.

ETL is massively used by Windows system programmers to log useful artifacts:
* `C:\Windows\System32\WDI\LogFiles\BootPerfDiagLogger.etl`
* `C:\Windows\System32\WDI\LogFiles\ShutdownPerfDiagLogger.etl`
* `NetTrace.etl` via `netsh`
* `C:\Windows\System32\WDI\<GUID>\<GUID>\snapshot.etl`
* etc.

A lot of new APIs such as `Tracelogging` or `WPP` are based on ETW. These APIs are used extensively by Microsoft developers for Windows. `Tracelogging` is addressed by `etl-parser`, `WPP` will be addressed in a future release.

Microsoft offers a lot of consumers that create ETL traces, such as `xperf.exe`, `logman.exe`, `netsh.exe`, etc.

We believe it is a gold mine for DFIR analysts.

## Credits

- This project is under copyright of the [Airbus Computer Emergency Response Team (CERT)](https://www.trusted-introducer.org/directory/teams/ai-cert.html) and distributed under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license
- [Geoff Chappel](https://www.geoffchappell.com/) for all information on his blog

## License

`etl-parser` is released under the [Apache 2.0](https://www.apache.org/licenses/LICENSE-2.0) license.