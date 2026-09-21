#include <android/binder_manager.h>
#include <android/binder_process.h>
#include <android/binder_status.h>
#include <log/log.h>
#include <sys/types.h>
#include <unistd.h>

#include <atomic>
#include <chrono>
#include <thread>

namespace {
std::atomic<bool> g_running{true};

void health_loop() {
    while (g_running.load()) {
        // Native health heartbeat only. No privileged policy decisions occur here.
        ALOGI("Buipui core heartbeat pid=%d uid=%d", getpid(), getuid());
        std::this_thread::sleep_for(std::chrono::seconds(30));
    }
}
}

int main() {
    ALOGI("Buipui native core starting");

    // Reserve Binder thread-pool capacity for the future stable AIDL interface.
    ABinderProcess_setThreadPoolMaxThreadCount(4);
    ABinderProcess_startThreadPool();

    health_loop();

    ABinderProcess_joinThreadPool();
    return 0;
}
