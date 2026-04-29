```mermaid
journey
    title Flow ITAM - User Stories

    section Organization Management
      Create organization: 5: Admin
      Manage organization settings: 4: Admin

    section User Management
      Add user: 5: Admin
      Update user details: 4: Admin
      Assign roles to user: 4: Admin
      Deactivate user: 3: Admin

    section Asset Management
      Add asset: 5: Admin, IT Staff
      Update asset details: 4: Admin, IT Staff
      View asset inventory: 5: Admin, IT Staff
      Categorize asset type: 4: Admin, IT Staff
      Track asset status: 5: Admin, IT Staff

    section Assignment Management
      Assign asset to user: 5: IT Staff
      View assigned assets: 5: Admin, IT Staff
      Return asset: 5: IT Staff
      View assignment history: 4: Admin, IT Staff

    section Location & Vendor
      Add location: 4: Admin
      Assign asset to location: 4: IT Staff
      Add vendor: 3: Admin
      Link vendor to asset: 3: IT Staff

    section Maintenance Tracking
      Log maintenance event: 4: IT Staff
      View maintenance history: 4: Admin, IT Staff

    section Software & Licensing
      Add software license: 4: Admin
      Track license seats: 4: Admin
      Assign software to asset: 4: IT Staff
      View license usage: 3: Admin

    section Reporting & Auditing
      Generate asset report: 5: Admin
      View unassigned assets: 5: Admin, IT Staff
      View audit logs: 4: Admin
      Track changes to assets: 4: Admin

    section Future API / Integration
      Access assets via API: 3: Developer
      Integrate with external systems: 2: Developer
```

