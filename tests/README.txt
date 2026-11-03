## Test Cases

## Input and Expeceted Recommendation

1. Input: ['portable', 'long_battery', 'budget_high', 'gaming', 'needs_ai_accel']
   --> Expected: recommended: high_end_gaming_laptop

2. Input: ['portable', 'long_battery', 'budget_high']
   --> Expected: recommended: premium_ultrabook

3. Input: ['gaming', 'creative_work', 'travel_often', 'prefer_os_macos', 'prefer_os_linux', 'needs_ai_accel']
   --> Expected: No recommendation could be made with the given facts.

4. Input: ['portable', 'long_battery', 'budget_high', 'gaming']
   --> Expected: recommended:  high_end_gaming_laptop and premium_ultrabook

5. Input ['budget_medium', 'gaming']
   --> Expected: recommended: midrange_gaming_laptop

6. Input ['portable', 'budget_low', 'creative_work', 'office_only', 'travel_often']
   --> Expected: recommended: budget_ultrabook

## Specs and Rule Trace

Whether a laptop is receommended or not, the specs the user needed for the laptop are displayed 
along with the rules that fired in order

1. Input['portable', 'large_screen', 'budget_medium', 'gaming', 'office_only', 'prefer_os_macos', 'needs_ai_accel']
   --> Expected: 
   Recommendation: midrange_gaming_laptop
>  Explanation: Derived from rule: Gaming

   Specifications:
   - macos_required
   - gpu_with_tensor_cores

   > Fired rules:
   1. GamingIF gaming AND budget_medium THEN recommend:midrange_gaming_laptop
   2. OS Preference MappingIF pref_os_macos THEN spec:macos_required
   3. AI AccelerationIF needs_ai_accel THEN spec:gpu_with_tensor_cores

2. Input['budget_low', 'gaming', 'creative_work', 'travel_often', 'prefer_os_linux', 'needs_ai_accel']
   --> Expected: 
   No recommendation could be made with the given facts.

   Specifications:
   - gpu_with_tensor_cores

   > Fired rules:
   1. AI AccelerationIF needs_ai_accel THEN spec:gpu_with_tensor_cores