class Track:
      # class level private variable tracking the instance count
      __instance_count = 0

      def __init__(self):
            Track.__instance_count += 1
            
      # class level method returning the instance count
      @classmethod
      def instance_count(cls):
            return cls.__instance_count

if __name__ == '__main__':

      # create 10 instances of Track()
      for i in range(1, 11):
            Track()

      # check if 10 instances are created
      if Track.instance_count() <> 10:
            raise ValueError('Should have 10 instances...')
