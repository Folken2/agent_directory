# Universal JSON Prompt Template for Image Generation
## Adaptive Framework for Multi-Vertical Applications

### Overview
This template provides a standardized JSON structure for image generation across diverse verticals (e-commerce, editorial, architecture, technical, creative, etc.). Each section includes:
- **Core Parameters** (mandatory across all verticals)
- **Vertical-Specific Modifiers** (contextual enhancements)
- **Customization Guidelines** (how to adapt for your industry)

---

## 1. MASTER TEMPLATE STRUCTURE

```json
{
  "metadata": {
    "project_name": "string",
    "vertical": "e-commerce|editorial|architecture|technical|creative|advertising|social_media|medical|other",
    "use_case": "string",
    "target_audience": "string",
    "version": "1.0",
    "created_date": "YYYY-MM-DD",
    "notes": "string"
  },
  "subject": {
    "primary": {
      "type": "string",
      "description": "string",
      "details": {
        "key_characteristics": ["array"],
        "materials": ["array"],
        "condition": "string",
        "size_relative": "string"
      },
      "pose_action": "string",
      "framing": "full_body|medium_shot|close_up|macro|wide_shot"
    },
    "secondary_elements": [
      {
        "type": "string",
        "description": "string",
        "relationship_to_primary": "string",
        "prominence": "background|secondary|tertiary"
      }
    ],
    "props_and_accessories": [
      {
        "item": "string",
        "material": "string",
        "placement": "string",
        "importance": "essential|supporting|decorative"
      }
    ]
  },
  "environment": {
    "setting": {
      "type": "indoor|outdoor|hybrid|abstract|studio",
      "location": "string",
      "description": "string",
      "time_period": "historical|contemporary|future|timeless"
    },
    "atmosphere": {
      "mood": "string",
      "weather_condition": "string",
      "air_quality": "clear|hazy|foggy|smoky|other",
      "season": "spring|summer|autumn|winter|not_applicable"
    },
    "background": {
      "treatment": "sharp|soft_blur|strong_bokeh|abstract|pattern|solid_color|gradient",
      "color_palette": ["hex_color_codes"],
      "elements": "string",
      "depth": "shallow|medium|deep|layered"
    },
    "spatial_arrangement": {
      "foreground": "string",
      "midground": "string",
      "background": "string",
      "spatial_logic": "string"
    }
  },
  "style": {
    "visual_aesthetic": {
      "primary_style": "photorealistic|illustration|digital_art|painting|mixed_media|minimalist|maximalist|abstract|other",
      "art_direction": ["array of style references"],
      "artistic_movement": "string",
      "era_reference": "string"
    },
    "color_treatment": {
      "grading": "warm|cool|neutral|vibrant|desaturated|monochrome",
      "color_palette": {
        "primary": ["hex_codes"],
        "secondary": ["hex_codes"],
        "accent": ["hex_codes"]
      },
      "saturation_level": "desaturated|natural|vivid|hyper_saturated",
      "contrast": "low|medium|high|very_high"
    },
    "texture_and_finish": {
      "surface_quality": "smooth|rough|grainy|glossy|matte|metallic|fabric",
      "material_properties": "string",
      "detail_level": "minimal|moderate|highly_detailed|hyper_realistic"
    },
    "effects": {
      "special_effects": ["array"],
      "filters": "string",
      "post_processing": "string",
      "quality_keywords": ["masterpiece", "professional", "high_detail", "ultra_realistic"]
    }
  },
  "camera": {
    "lens": {
      "focal_length": "10mm|14mm|24mm|35mm|50mm|85mm|135mm|200mm|macro_100mm|other",
      "lens_type": "wide_angle|standard|telephoto|macro|fisheye|tilt_shift"
    },
    "depth_of_field": {
      "aperture": "f/1.4|f/2.8|f/4|f/5.6|f/8|f/11|f/16|other",
      "focus_point": "string",
      "blur_amount": "shallow|medium|deep|everything_in_focus"
    },
    "angle_and_perspective": {
      "horizontal_angle": "straight_on|45_degree_left|45_degree_right|90_left|90_right|other",
      "vertical_angle": "eye_level|low_angle_looking_up|high_angle_looking_down|bird_eye|worm_eye",
      "perspective_type": "linear|wide_angle_distortion|compressed|isometric|other",
      "tilt": "level|slight_tilt|canted|dutch_angle|other"
    },
    "composition": {
      "rule": "rule_of_thirds|centered|diagonal|golden_ratio|symmetrical|asymmetrical|leading_lines|frame_within_frame",
      "framing_technique": "close_cropped|standard|loose|negative_space_heavy",
      "subject_placement": "string"
    },
    "aspect_ratio": "1:1|4:3|16:9|9:16|21:9|3:2|2:3|custom",
    "resolution_target": "1K|2K|4K|8K|native_high_detail"
  },
  "lighting": {
    "primary_light_source": {
      "type": "natural_sunlight|window_light|studio_key_light|firelight|neon|led|practical_source|combination",
      "direction": "front|front_left_45|left_90|back_left_135|back_180|back_right_135|right_90|front_right_45|top|bottom|omnidirectional",
      "quality": "hard|soft|diffused|semi_diffused",
      "intensity": "weak|moderate|strong|very_strong",
      "color_temperature": "warm_2700k|neutral_5500k|cool_6500k|very_cool_8000k|mixed"
    },
    "secondary_light_sources": [
      {
        "type": "fill_light|rim_light|accent_light|background_light|other",
        "direction": "string",
        "intensity": "weak|moderate|strong",
        "color": "string"
      }
    ],
    "shadows": {
      "shadow_quality": "crisp|soft|undefined",
      "shadow_depth": "shallow|moderate|deep|very_deep",
      "shadow_color": "pure_black|cool_blue|warm_brown|other"
    },
    "time_of_day": "sunrise|golden_hour|midday|afternoon|blue_hour|dusk|sunset|twilight|night|artificial_light_only",
    "lighting_style": "studio_controlled|natural|mixed|dramatic|flat|rim_lit|backlighting|side_lighting|three_point",
    "special_lighting_effects": {
      "volumetric_light": "boolean",
      "god_rays": "boolean",
      "lens_flare": "boolean",
      "glow": "boolean",
      "bloom": "boolean",
      "other_effects": ["array"]
    }
  },
  "composition_advanced": {
    "depth_layering": {
      "foreground_depth": "string",
      "midground_depth": "string",
      "background_depth": "string",
      "air_perspective": "boolean",
      "atmospheric_depth": "clear|slight_haze|moderate_haze|heavy_fog"
    },
    "visual_balance": "symmetrical|asymmetrical|radial|dynamic",
    "visual_weight_distribution": "string",
    "movement_and_flow": "static|flowing|dynamic|circular|diagonal",
    "focal_point_hierarchy": [
      {
        "element": "string",
        "priority": 1,
        "draw_method": "contrast|size|color|isolation|other"
      }
    ],
    "empty_space_treatment": "minimalist|breathing_room|balanced|filled",
    "edge_treatment": "clean_edges|soft_edges|vignette|fade_to_white|fade_to_black|organic_edges"
  },
  "technical_specifications": {
    "rendering_engine": "photorealistic|3d_rendered|illustration|mixed|other",
    "quality_standards": {
      "sharpness": "soft_focus|slightly_soft|sharp|razor_sharp|hyper_sharp",
      "detail_level": "low|moderate|high|ultra_high|hyper_detailed",
      "texture_fidelity": "low|moderate|high|photographic",
      "material_accuracy": "approximated|realistic|hyper_realistic|scientifically_accurate"
    },
    "output_format": "standard|wide|tall|square|cinematic",
    "processing_style": "raw|slightly_edited|professionally_edited|heavily_stylized",
    "noise_and_artifacts": "none|minimal|absent_of_compression",
    "reference_media": [
      {
        "type": "film|photograph|artwork|brand|aesthetic|mood",
        "reference": "string",
        "influence_level": "subtle|moderate|strong"
      }
    ]
  },
  "negative_constraints": {
    "visual_artifacts": [
      "low_resolution",
      "blurry",
      "pixelated",
      "compression_artifacts",
      "noise",
      "jpeg_artifacts"
    ],
    "anatomical_errors": [
      "extra_limbs",
      "extra_fingers",
      "deformed_hands",
      "distorted_face",
      "unnatural_proportions",
      "missing_limbs"
    ],
    "unwanted_elements": [
      "text",
      "watermark",
      "signature",
      "logo",
      "border",
      "frame"
    ],
    "style_conflicts": [
      "cartoon_if_photorealistic_requested",
      "anime_if_realistic_requested",
      "sketch_if_polished_requested"
    ],
    "quality_issues": [
      "harsh_shadows",
      "overexposed",
      "underexposed",
      "flat_lighting",
      "unnatural_colors",
      "washed_out"
    ],
    "content_exclusions": [
      "other_people",
      "complex_backgrounds",
      "distracting_elements"
    ],
    "custom_exclusions": []
  },
  "reference_images": [
    {
      "image_id": "ref_001",
      "purpose": "style_reference|character_consistency|composition_guide|material_properties|lighting_reference|mood_reference",
      "influence_weight": 0.0,
      "apply_to": ["array of applicable elements"],
      "preserve": ["array of elements to maintain exactly"],
      "allow_variation": ["array of elements that can change"]
    }
  ],
  "generation_parameters": {
    "model": "gemini_nano_banana|gemini_nano_banana_pro|gemini_2_5_flash_image|other",
    "cfg_scale": 7.0,
    "sampling_steps": 30,
    "seed": "random_or_specific_number",
    "temperature": 0.7,
    "aspect_ratio": "4:3",
    "thinking_mode_enabled": false,
    "quality_preset": "balanced|quality_optimized|speed_optimized"
  },
  "context_and_requirements": {
    "brand_guidelines": {
      "brand_name": "string",
      "color_palette": ["hex_codes"],
      "typography_style": "string",
      "brand_voice": "string",
      "must_include_elements": ["array"],
      "must_exclude_elements": ["array"]
    },
    "platform_requirements": {
      "platform": "instagram|facebook|tiktok|twitter|linkedin|website|print|other",
      "optimal_dimensions": "string",
      "content_guidelines": "string",
      "performance_goals": "engagement|conversion|brand_awareness|other"
    },
    "success_criteria": {
      "what_makes_it_successful": "string",
      "key_evaluation_metrics": ["array"],
      "acceptable_variations": "string"
    },
    "constraints": {
      "budget_considerations": "string",
      "timeline": "string",
      "legal_compliance": "string",
      "cultural_sensitivity": "string"
    }
  },
  "vertical_specific_settings": {
    "e_commerce": {
      "product_focus": "hero_image|lifestyle|detail_shot|scale_reference|context_usage",
      "background_treatment": "white|lifestyle|pattern|gradient",
      "lifestyle_context": "boolean",
      "size_scale_reference": "boolean",
      "multiple_angles": false,
      "packaging_visibility": "boolean"
    },
    "editorial": {
      "story_context": "string",
      "emotional_tone": "string",
      "headline_compatibility": "boolean",
      "text_overlay_space": "none|minimal|moderate|significant",
      "magazine_spread_type": "cover|feature|sidebar|full_page|double_page"
    },
    "architecture": {
      "view_type": "exterior|interior|detail|aerial|sectional_cutaway",
      "furnishing_level": "unfurnished|partially_furnished|fully_furnished",
      "occupancy": "empty|sparse|normal_use|busy",
      "time_of_day_priority": "daytime|golden_hour|night|flexible",
      "weather_conditions": "clear|overcast|seasonal_specific"
    },
    "technical": {
      "diagram_type": "flowchart|schematic|isometric|exploded_view|cross_section|other",
      "annotation_level": "minimal|moderate|comprehensive",
      "text_accuracy": "mandatory_exact_labels",
      "component_accuracy": "conceptual|realistic|technical_specification",
      "color_coding": "boolean"
    },
    "creative": {
      "narrative_element": "string",
      "emotional_resonance": "string",
      "metaphorical_content": "boolean",
      "artistic_freedom": "high|moderate|constrained",
      "surrealism_level": "none|subtle|moderate|strong"
    },
    "advertising": {
      "campaign_message": "string",
      "call_to_action_implied": "string",
      "target_demographic": "string",
      "emotional_trigger": "joy|trust|urgency|aspiration|other",
      "celebrity_or_influencer_style": "string"
    },
    "social_media": {
      "platform_specific_format": "instagram_square|instagram_reel|tiktok|youtube_thumbnail|twitter_header|linkedin_post|pinterest_pin",
      "trend_alignment": "string",
      "visual_hook": "bold_color|movement_implied|surprise_element|other",
      "text_integration": "none|minimal|integrated|overlay_ready",
      "scrollstopping_element": "string"
    },
    "medical_scientific": {
      "accuracy_level": "educational|clinical|research_grade",
      "anatomical_detail": "general|moderate|precise",
      "labeling_requirements": "minimal|comprehensive|interactive_ready",
      "reference_standards": "medical_textbook|clinical_photography|scientific_illustration",
      "patient_representation": "diverse|age_range|condition_specific"
    }
  },
  "iteration_tracking": {
    "iteration_number": 1,
    "changes_from_previous": "string",
    "performance_notes": "string",
    "issues_to_address_next": ["array"],
    "successful_elements": ["array"],
    "unsuccessful_elements": ["array"]
  }
}
```

---

## 2. VERTICAL-SPECIFIC ADAPTATION GUIDES

### 2.1 E-COMMERCE

**Use Case**: Product photography, lifestyle imagery, hero images

**Key Modifications**:

```json
{
  "metadata": {
    "vertical": "e-commerce",
    "use_case": "product_hero_image"
  },
  "subject": {
    "primary": {
      "type": "product",
      "details": {
        "product_name": "string",
        "materials": ["glass", "metal", "fabric"],
        "finish": "matte|glossy|brushed|textured",
        "surface_condition": "new|pristine|used|worn"
      }
    }
  },
  "environment": {
    "background": {
      "treatment": "white|marble|wood|lifestyle_contextual",
      "color_palette": ["#FFFFFF"],
      "elements": "minimal"
    }
  },
  "lighting": {
    "lighting_style": "studio_controlled",
    "primary_light_source": {
      "type": "studio_key_light",
      "direction": "45_degree_left",
      "quality": "semi_diffused"
    },
    "secondary_light_sources": [
      {
        "type": "fill_light",
        "intensity": "moderate"
      },
      {
        "type": "rim_light",
        "intensity": "moderate"
      }
    ]
  },
  "vertical_specific_settings": {
    "e_commerce": {
      "product_focus": "hero_image",
      "background_treatment": "white",
      "lifestyle_context": false,
      "size_scale_reference": false,
      "packaging_visibility": true
    }
  },
  "negative_constraints": {
    "unwanted_elements": [
      "text",
      "watermark",
      "brand_competitor_logos",
      "distracting_background",
      "people",
      "harsh_shadows"
    ]
  }
}
```

**Customization Checklist**:
- ✅ Set background to white, marble, or lifestyle context
- ✅ Specify product material properties (glass transparency, fabric texture, metal finish)
- ✅ Include scale reference if needed (person's hand, ruler, contextual object)
- ✅ Use professional studio lighting (45-degree key light, fill, rim)
- ✅ Choose hero_image or lifestyle for primary focus
- ✅ Exclude people if product-only shot required

---

### 2.2 EDITORIAL / MAGAZINE

**Use Case**: Magazine covers, article imagery, visual storytelling

```json
{
  "metadata": {
    "vertical": "editorial",
    "use_case": "magazine_cover"
  },
  "subject": {
    "primary": {
      "framing": "medium_shot|close_up"
    }
  },
  "environment": {
    "atmosphere": {
      "mood": "compelling|engaging|aspirational",
      "narrative_context": "string"
    }
  },
  "composition_advanced": {
    "focal_point_hierarchy": [
      {
        "element": "subject_face",
        "priority": 1,
        "draw_method": "eye_contact|emotion|contrast"
      }
    ],
    "empty_space_treatment": "breathing_room"
  },
  "technical_specifications": {
    "reference_media": [
      {
        "type": "magazine",
        "reference": "Vogue|Elle|National Geographic|specific_publication"
      }
    ]
  },
  "vertical_specific_settings": {
    "editorial": {
      "story_context": "brief_narrative_or_theme",
      "emotional_tone": "aspirational|investigative|intimate|dramatic",
      "text_overlay_space": "significant",
      "magazine_spread_type": "cover"
    }
  },
  "context_and_requirements": {
    "platform_requirements": {
      "platform": "print",
      "content_guidelines": "magazine_editorial_standards"
    }
  }
}
```

**Customization Checklist**:
- ✅ Define emotional tone (aspirational, intimate, dramatic, investigative)
- ✅ Leave space for headline text overlay
- ✅ Create strong focal point for eye direction
- ✅ Choose appropriate magazine reference aesthetic
- ✅ Ensure subject's expression communicates story tone
- ✅ Consider cultural representation and diversity

---

### 2.3 ARCHITECTURE / INTERIOR DESIGN

**Use Case**: Space visualization, real estate, architectural renders

```json
{
  "metadata": {
    "vertical": "architecture",
    "use_case": "interior_visualization"
  },
  "subject": {
    "primary": {
      "type": "space",
      "description": "living_room|bedroom|kitchen|office|restaurant",
      "details": {
        "style": "scandinavian|industrial|modern|traditional|eclectic",
        "color_scheme": "neutral|warm|cool|mixed",
        "furnishing_style": "minimalist|maximalist|balanced"
      }
    }
  },
  "environment": {
    "setting": {
      "type": "indoor",
      "location": "residential|commercial|hospitality"
    },
    "spatial_arrangement": {
      "foreground": "furniture_piece",
      "midground": "space_center",
      "background": "walls_windows_architecture"
    }
  },
  "camera": {
    "angle_and_perspective": {
      "horizontal_angle": "45_degree_left",
      "vertical_angle": "eye_level",
      "perspective_type": "linear"
    }
  },
  "lighting": {
    "time_of_day": "golden_hour|afternoon|natural_daylight",
    "primary_light_source": {
      "type": "window_light",
      "direction": "natural_directional"
    }
  },
  "vertical_specific_settings": {
    "architecture": {
      "view_type": "interior",
      "furnishing_level": "fully_furnished",
      "occupancy": "empty|sparse",
      "weather_conditions": "clear"
    }
  },
  "technical_specifications": {
    "material_accuracy": "realistic"
  }
}
```

**Customization Checklist**:
- ✅ Specify interior style (Scandinavian, Industrial, Modern, etc.)
- ✅ Choose view type (exterior, interior, aerial, detail)
- ✅ Define furnishing level and occupancy
- ✅ Set appropriate time of day for lighting mood
- ✅ Ensure spatial logic makes architectural sense
- ✅ Maintain realistic material properties (wood, tile, fabric)

---

### 2.4 TECHNICAL / SCIENTIFIC DIAGRAMS

**Use Case**: Infographics, schematics, exploded views, technical illustrations

```json
{
  "metadata": {
    "vertical": "technical",
    "use_case": "technical_diagram"
  },
  "subject": {
    "primary": {
      "type": "system|component|process",
      "details": {
        "technical_accuracy": "essential",
        "components": ["component_list"],
        "functionality": "string"
      }
    }
  },
  "style": {
    "visual_aesthetic": {
      "primary_style": "technical_illustration|isometric_diagram|schematic",
      "detail_level": "moderate|high"
    },
    "color_treatment": {
      "color_palette": {
        "primary": ["#0066CC"],
        "secondary": ["#FF6600"],
        "accent": ["#00CC66"]
      }
    }
  },
  "camera": {
    "angle_and_perspective": {
      "perspective_type": "isometric|exploded_view|sectional"
    }
  },
  "lighting": {
    "lighting_style": "technical_neutral",
    "special_lighting_effects": {
      "volumetric_light": false,
      "glow": true
    }
  },
  "technical_specifications": {
    "quality_standards": {
      "text_accuracy": "essential",
      "material_accuracy": "technical_specification"
    }
  },
  "vertical_specific_settings": {
    "technical": {
      "diagram_type": "isometric|schematic|exploded_view",
      "annotation_level": "comprehensive",
      "text_accuracy": "mandatory_exact_labels",
      "component_accuracy": "technical_specification",
      "color_coding": true
    }
  },
  "negative_constraints": {
    "unwanted_elements": [
      "photorealistic_textures",
      "ambient_background",
      "people",
      "organic_elements"
    ]
  }
}
```

**Customization Checklist**:
- ✅ Choose diagram type (isometric, exploded, sectional, schematic)
- ✅ Define color coding scheme for component categories
- ✅ Ensure text labels are exact and legible
- ✅ Maintain technical accuracy for all components
- ✅ Use clean, neutral background
- ✅ Apply consistent style across all elements
- ✅ Include annotation level appropriate for audience

---

### 2.5 ADVERTISING / MARKETING

**Use Case**: Ad campaigns, promotional imagery, brand assets

```json
{
  "metadata": {
    "vertical": "advertising",
    "use_case": "product_advertisement"
  },
  "subject": {
    "primary": {
      "type": "product|lifestyle|emotional_concept"
    }
  },
  "style": {
    "visual_aesthetic": {
      "art_direction": ["brand_aesthetic", "trending_style", "emotional_resonance"]
    }
  },
  "composition_advanced": {
    "visual_balance": "dynamic",
    "focal_point_hierarchy": [
      {
        "element": "product|call_to_action",
        "priority": 1
      }
    ]
  },
  "vertical_specific_settings": {
    "advertising": {
      "campaign_message": "clear_value_proposition",
      "call_to_action_implied": "purchase|discover|experience|learn_more",
      "target_demographic": "age_range|lifestyle|values",
      "emotional_trigger": "aspiration|joy|trust|urgency"
    }
  },
  "context_and_requirements": {
    "platform_requirements": {
      "platform": "instagram|facebook|google_ads|billboard",
      "performance_goals": "engagement|conversion|brand_awareness"
    },
    "brand_guidelines": {
      "must_include_elements": ["logo_placement", "color_palette", "brand_message"]
    }
  }
}
```

**Customization Checklist**:
- ✅ Clearly define brand messaging and campaign objectives
- ✅ Choose emotional triggers (joy, trust, aspiration, urgency)
- ✅ Define target demographic and lifestyle
- ✅ Specify platform requirements (Instagram, billboard, etc.)
- ✅ Include brand elements (logo, colors, typography)
- ✅ Design for primary platform dimensions
- ✅ Create visual hook for stopping scrolling

---

### 2.6 SOCIAL MEDIA

**Use Case**: Instagram, TikTok, LinkedIn, Twitter, Pinterest

```json
{
  "metadata": {
    "vertical": "social_media",
    "use_case": "instagram_post"
  },
  "camera": {
    "aspect_ratio": "1:1"
  },
  "composition_advanced": {
    "empty_space_treatment": "minimal",
    "visual_weight_distribution": "dynamic"
  },
  "style": {
    "effects": {
      "quality_keywords": ["scroll_stopping", "visually_bold", "immediately_engaging"]
    }
  },
  "vertical_specific_settings": {
    "social_media": {
      "platform_specific_format": "instagram_square",
      "trend_alignment": "current_aesthetic_trend",
      "visual_hook": "bold_color|surprising_composition|movement_implied",
      "text_integration": "minimal|overlay_ready"
    }
  }
}
```

**Customization Checklist**:
- ✅ Choose platform (Instagram, TikTok, LinkedIn, etc.)
- ✅ Set correct aspect ratio for platform
- ✅ Create visual hook for algorithm engagement
- ✅ Align with current trend aesthetic
- ✅ Design for mobile viewing
- ✅ Consider text overlay spacing
- ✅ Optimize for scrolling attention-grabbing

---

### 2.7 MEDICAL / SCIENTIFIC

**Use Case**: Educational illustrations, clinical documentation, research visualization

```json
{
  "metadata": {
    "vertical": "medical_scientific",
    "use_case": "anatomical_illustration"
  },
  "subject": {
    "primary": {
      "type": "anatomical_structure|medical_process|scientific_phenomenon",
      "details": {
        "accuracy_level": "essential",
        "reference_standards": "medical_textbook|clinical_photography|scientific_illustration"
      }
    }
  },
  "style": {
    "visual_aesthetic": {
      "primary_style": "scientific_illustration|medical_rendering"
    }
  },
  "technical_specifications": {
    "quality_standards": {
      "material_accuracy": "scientifically_accurate"
    }
  },
  "vertical_specific_settings": {
    "medical_scientific": {
      "accuracy_level": "clinical|research_grade",
      "anatomical_detail": "precise",
      "labeling_requirements": "comprehensive",
      "reference_standards": "medical_textbook",
      "patient_representation": "diverse"
    }
  },
  "negative_constraints": {
    "custom_exclusions": [
      "inaccurate_anatomy",
      "stylization_over_accuracy",
      "sensationalism"
    ]
  }
}
```

**Customization Checklist**:
- ✅ Ensure scientific/medical accuracy as priority
- ✅ Reference appropriate medical standards and textbooks
- ✅ Include comprehensive anatomical labeling
- ✅ Use accurate color representation
- ✅ Consider patient diversity and representation
- ✅ Maintain clarity for educational/clinical use

---

## 3. CUSTOMIZATION WORKFLOW

### Step 1: Select Your Vertical
Choose from predefined verticals or create hybrid approach:
- Primary vertical (dominant)
- Secondary vertical (supporting elements)

### Step 2: Start with Master Template
Copy the complete master template structure.

### Step 3: Apply Vertical-Specific Settings
Replace generic `vertical_specific_settings` section with your vertical's preset.

### Step 4: Customize Core Parameters
Modify primary sections:
- `subject`: What is being created
- `environment`: Where and context
- `style`: How it should look
- `camera`: Visual framing
- `lighting`: Illumination approach

### Step 5: Set Context Requirements
Complete `context_and_requirements`:
- Brand guidelines (if applicable)
- Platform requirements
- Success criteria
- Constraints

### Step 6: Validate and Test
1. Verify JSON syntax (use jsonlint.com)
2. Generate test image
3. Compare against success criteria
4. Iterate and refine

### Step 7: Document and Version
Save template with version number and notes for future reference.

---

## 4. QUICK REFERENCE: VERTICAL PARAMETERS

| Vertical | Primary Focus | Key Parameters | Best Practices |
|----------|---------------|-----------------|-----------------|
| **E-Commerce** | Product clarity | Background, lighting, scale | White/lifestyle backgrounds, studio lighting |
| **Editorial** | Story & emotion | Mood, composition, space | Breathing room, headline compatibility, emotional tone |
| **Architecture** | Space & design | View type, furnishing, daylight | Realistic materials, proper perspective, lighting mood |
| **Technical** | Accuracy & clarity | Diagram type, color coding, labels | Isometric/exploded views, comprehensive annotations |
| **Advertising** | Engagement & CTA | Emotional trigger, platform, demographics | Dynamic composition, brand alignment, trend-aware |
| **Social Media** | Scroll-stopping | Visual hook, aspect ratio, engagement | Bold colors, immediate visual impact, platform-specific |
| **Medical/Scientific** | Accuracy & education | Anatomical precision, labeling, standards | Medical textbook references, diverse representation, labels |

---

## 5. ADVANCED TECHNIQUES

### 5.1 Multi-Product Composition (E-Commerce)

```json
{
  "subject": {
    "primary": {
      "type": "primary_product"
    },
    "secondary_elements": [
      {
        "type": "complementary_product",
        "relationship_to_primary": "pairs_with_primary",
        "prominence": "secondary"
      }
    ]
  },
  "composition_advanced": {
    "focal_point_hierarchy": [
      {"element": "primary_product", "priority": 1},
      {"element": "secondary_product", "priority": 2}
    ]
  }
}
```

### 5.2 Narrative Sequences (Editorial/Creative)

```json
{
  "iteration_tracking": {
    "sequence_number": 1,
    "narrative_connection": "story_progression"
  },
  "subject": {
    "primary": {
      "action_sequence": "before|action|after|consequence"
    }
  }
}
```

### 5.3 Seasonal Variations (All Verticals)

```json
{
  "environment": {
    "atmosphere": {
      "season": "spring|summer|autumn|winter"
    }
  }
}
```

Use same prompt structure with only seasonal modifications to maintain consistency.

### 5.4 Reference-Based Character Consistency

```json
{
  "reference_images": [
    {
      "image_id": "character_base_001",
      "purpose": "character_consistency",
      "influence_weight": 0.9,
      "preserve": ["facial_features", "eye_color", "hair_texture"],
      "allow_variation": ["clothing", "expression", "lighting"]
    }
  ]
}
```

---

## 6. TROUBLESHOOTING COMMON ISSUES

| Issue | Cause | Solution |
|-------|-------|----------|
| Output doesn't match vertical | Wrong vertical settings applied | Verify `vertical_specific_settings` match chosen vertical |
| Colors look wrong | Incorrect color_treatment | Check `color_treatment.grading` and palette hex codes |
| Lighting feels flat | Insufficient light source definition | Add secondary lights (fill, rim, accent) with specific intensity |
| Composition is awkward | Poor focal point hierarchy | Redefine focal_point_hierarchy with clear priority order |
| Text contains errors | Unclear text specifications | Use `text_accuracy: "mandatory_exact_labels"` and specify each text element |
| Style inconsistent | Conflicting aesthetic directions | Remove contradictory style references, use single cohesive aesthetic |
| Image lacks depth | Missing layering information | Define foreground, midground, background clearly in composition |

---

## 7. VERSION HISTORY & UPDATES

**Current Version**: 1.0 (December 2025)

### Future Enhancements (Roadmap)
- [ ] Real-time JSON validation tool integration
- [ ] AI-powered prompt optimization suggestions
- [ ] Community template library
- [ ] Automated batch generation scripts
- [ ] Performance metrics dashboard
- [ ] A/B testing framework for prompt comparison
- [ ] Brand asset management integration
- [ ] Multi-language support

---

## 8. BEST PRACTICES SUMMARY

✅ **DO:**
- Start with clear vertical definition
- Use specific, measurable descriptors
- Validate JSON syntax before generation
- Test with reference images for consistency
- Document successful prompts for future use
- Iterate incrementally, changing one parameter at a time
- Version control your prompt templates
- Include both positive and negative constraints

❌ **DON'T:**
- Over-nest JSON structure (keep hierarchy 2-3 levels deep)
- Mix conflicting aesthetic directions (photorealistic + cartoon)
- Forget negative constraints
- Use vague descriptors ("nice colors", "good lighting")
- Skip validation and testing
- Ignore platform-specific requirements
- Assume first generation is perfect
- Modify multiple parameters simultaneously during iteration

---

**Template Created**: December 4, 2025
**Compatible Models**: Gemini Nano Banana, Nano Banana Pro, Gemini 2.5 Flash Image
**Maintenance**: Update verticals as new use cases emerge