-- Pandoc Lua filter to set default font for DOCX output
-- Usage: pandoc input.md -o output.docx --lua-filter=docx_font_filter.lua -M docx-font="Times New Roman" -M docx-fontsize="12pt"

function get_metadata_value(meta, key, default)
    if meta[key] then
        return pandoc.utils.stringify(meta[key])
    else
        return default
    end
end

function Meta(meta)
    -- Get font settings from metadata
    local font = get_metadata_value(meta, 'docx-font', nil)
    local fontsize = get_metadata_value(meta, 'docx-fontsize', nil)
    
    -- Store in global variables for use in Inline function
    if font then
        PANDOC_STATE.docx_font = font
    end
    if fontsize then
        PANDOC_STATE.docx_fontsize = fontsize
    end
    
    return meta
end

-- Apply font to all text
function Span(el)
    local font = PANDOC_STATE.docx_font
    local fontsize = PANDOC_STATE.docx_fontsize
    
    if font or fontsize then
        local attrs = {}
        if font then
            table.insert(attrs, {'custom-style', font})
        end
        el.attributes = attrs
        return el
    end
end

-- Apply font to paragraphs
function Para(el)
    local font = PANDOC_STATE.docx_font
    
    if font then
        -- Wrap content with font information
        local formatted_content = {}
        for _, item in ipairs(el.content) do
            table.insert(formatted_content, item)
        end
        el.content = formatted_content
        return el
    end
end

return {
    {Meta = Meta},
    {Span = Span, Para = Para}
}



