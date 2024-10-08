from typing import Any,Optional
from wildlife_tracker.migration_tracking.migration_path import MigrationPath
from wildlife_tracker.habitat_management.habitat import Habitat 

class Migration:

#formal and put migration path in migration path 

  def __init__(self,current_date: str,
               migration_id: int,
               current_location: str,
               duration:Optional[int] = None)-> None:
    
    self.current_date=current_date
    self.current_location=current_location
    self.migration_id=migration_id
    self.duration=duration

               

  def update_migration_details(migration_id: int, **kwargs: Any) -> None:
   pass
   
   def get_migration_details(migration_id: int) -> dict[str, Any]:
        pass 
   
   