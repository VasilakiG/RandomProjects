add_library(EventCounterLib STATIC EventCounter.cpp)

target_include_directories(EventCounterLib PUBLIC ${CMAKE_CURRENT_SOURCE_DIR})