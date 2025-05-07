
#include <LibELF/Image.h>
#include <stddef.h>
#include <stdint.h>

extern "C" int LLVMFuzzerTestOneInput(uint8_t const* data, size_t size)
{
    AK::set_debug_enabled(false);
    ELF::Image elf(data, size, /*verbose_logging=*/false);
    if (!elf.is_valid())
        return 0;
    
    elf.for_each_section([](auto const& section) {
        auto name = section.name();  // Safe access to section names
        (void)name;
        auto size = section.size();  // Access metadata
        (void)size;
        auto bytes = section.bytes();  // Safe raw access
        (void)bytes;
    });

    auto maybe_text = elf.lookup_section(AK::StringView(".text", strlen(".text")));
    if (maybe_text.has_value()) {
        auto text_section = maybe_text.value();
        auto text_data = text_section.bytes();
        (void)text_data;
    }
    return 0;
}
